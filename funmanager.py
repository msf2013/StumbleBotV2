import requests
import json
import random
import threading
import http.client
from bs4 import BeautifulSoup

tokesstarted = False
bitcoinbotstarted = False
# Create a lock object for thread-safe operations
bitcoinbot_lock = threading.Lock()
lastprice = ""

commandlist = ['joke','']


import wikipediaapi


def get_movie(name, api_key, max_length=350):
    # Replace spaces in the movie name with '+' for URL compatibility
    query = name.replace(" ", "+")
    url = f"http://www.omdbapi.com/?t={query}&apikey={api_key}"
    
    # Make the request to the OMDb API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        
        # Check if the movie was found
        if data["Response"] == "True":
            # Get the plot and truncate if necessary
            summary = data.get("Plot", "Description not available.")
            if len(summary) > max_length:
                summary = summary[:max_length].rsplit(' ', 1)[0] + '...'
            return summary
        else:
            return "Movie not found."
    else:
        return "Failed to connect to the OMDb API."
def get_wikipedia_summary(title, max_length=350):
    # Create a Wikipedia API object for the English language
    wiki_wiki = wikipediaapi.Wikipedia('en')
    
    # Get the page object for the given title
    page = wiki_wiki.page(title)
    
    # Retrieve the summary
    summary = page.summary

    # Truncate the summary to the desired length if necessary
    if len(summary) > max_length:
        summary = summary[:max_length].rsplit(' ', 1)[0] + '...'  # Truncate at the last complete word
    
    return summary

def get_horoscope_from_web(sign_id):
    url = f'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign={sign_id}'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find the element containing the horoscope text
        horoscope_text = soup.find('div', class_='main-horoscope').p.text
        return f'Horoscope says: {horoscope_text}'
    else:
        return "Failed to retrieve horoscope."

# Function to map zodiac sign to its corresponding ID on horoscope.com
def get_sign_id(sign):
    signs = {
        'aries': 1,
        'taurus': 2,
        'gemini': 3,
        'cancer': 4,
        'leo': 5,
        'virgo': 6,
        'libra': 7,
        'scorpio': 8,
        'sagittarius': 9,
        'capricorn': 10,
        'aquarius': 11,
        'pisces': 12
    }
    return signs.get(sign, None)
def HandleAdvice():
    url = "https://api.adviceslip.com/advice"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Will raise an exception for HTTP errors
        data = response.json()
        advice = data['slip']['advice']
        return f'Advice says: {advice}'
    except requests.exceptions.RequestException as e:
        print(f"Error fetching advice: {e}")
        return None

def HandleJoke():
    url = "https://v2.jokeapi.dev/joke/Dark,Pun?type=single"
    req = requests.get(url).text
    data = json.loads(req)

    # Check if the joke was successfully retrieved
    if data['error']:
        return "Error fetching joke."

    # Retrieve the joke text
    question = data['joke']
    return f'Joke: {question}'
def HandleUrb(search):
    if str(search).strip():
        urban_api_url = 'http://api.urbandictionary.com/v0/define?term=%s' % search
        g = requests.get(urban_api_url).text
        response_data = json.loads(g)['list'][0]
        response = response_data['definition']
        url = response_data['permalink']
        max_length = 350
        truncated_response = response[:max_length]  # Truncate to the first 450 characters
        final_message = f"{truncated_response}... Source: {url}"
        return f'{final_message}'   
def HandleRoll():
    choices = ['1', '2', '3', '4', '5', '6']
    rollu = random.choice(choices)
    rollb = random.choice(choices)
    if rollu < rollb:
        return f'You rolled: {rollu} Bot rolled:{rollb}\nYou Lose!'
    elif rollu == rollb:
        return f'You rolled: {rollu}\nBot rolled:{rollb} Roll was a draw!'
    else:     
        return f'🔥 You rolled: {rollu}\nBot rolled:{rollb} You win! 🔥'
def HandleFlip():
    choices = ['Heads', 'Tails']
    flip = random.choice(choices)
    return f'You flipped: {flip}'

def HandleBitcoins():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url).json()
    
    # Extract the price from the response
    price = response.get('bitcoin', {}).get('usd', 'Price not available')
    
    # Send the price as a public message
    return f"CryptoWatch says: ${price}"
def HandleLiteCoins():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd"
    response = requests.get(url).json()
    
    # Extract the price from the response
    price = response.get('litecoin', {}).get('usd', 'Price not available')
    
    # Send the price as a public message
    return f"CryptoWatch says: ${price}"
def HandleChuckNorris(): # YEA RIGHT! ~roundhouse

    url = "https://api.chucknorris.io/jokes/random"
    out = requests.get(url).text
    resp_dict = json.loads(out)
    results = resp_dict['value']
    return f"{results}"
def HandleMom():
    url = 'https://www.yomama-jokes.com/api/v1/jokes/random/'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        joke_data = response.json()
        #return joke_data['joke']
        return joke_data['joke']
    except requests.RequestException as e:
        return f"An error occurred: {e}"   
def HandleOneLiner():
    pickup_lines = [
        "Are you a magician? Because whenever I look at you, everyone else disappears.",
        "Do you have a map? Because I keep getting lost in your eyes.",
        "If you were a vegetable, you'd be a cute-cumber!",
        "Is your name Google? Because you have everything I’ve been searching for.",
        "Do you have a Band-Aid? Because I just scraped my knee falling for you.",
        "Are you a time traveler? Because I can see you in my future.",
        "If you were a fruit, you'd be a fineapple.",
        "Do you have a sunburn, or are you always this hot?",
        "Is your dad a baker? Because you’re a cutie pie!",
        "If you were a triangle, you’d be acute one.",
        "Do you have a quarter? Because I want to call my mom and tell her I met 'The One'.",
        "Are you made of copper and tellurium? Because you’re Cu-Te.",
        "If you were a burger at McDonald's, you'd be the McGorgeous.",
        "Do you have a name, or can I call you mine?",
        "Is your name Wi-Fi? Because I’m feeling a connection.",
        "Are you French? Because Eiffel for you.",
        "Do you like raisins? No? How about a date?",
        "Is your name Chapstick? Because you’re making my lips numb.",
        "If looks could kill, you’d definitely be a heartbreaker.",
        "I must be a snowflake, because I've fallen for you.",
        "Is your name Dunkin? Because I donut want to spend another day without you.",
        "Are you Australian? Because when I look at you, I feel like I’m down under.",
        "Are you a cat? Because I’m feline a connection.",
        "Is your name Starbucks? Because I like you a latte.",
        "If I could rearrange the alphabet, I’d put U and I together.",
        "Do you have a compass? Because I keep getting lost in your eyes.",
        "If you were a tear in my eye, I wouldn’t cry for fear of losing you.",
        "Are you a campfire? Because you’re hot and I want s'more.",
        "Is your name Eleven? Because you're definitely a ten.",
        "Do you have an eraser? Because I can’t get you out of my mind.",
        "Are you an angel? Because heaven is missing one.",
        "If beauty were time, you'd be an eternity.",
        "Is your last name Campbell? Because you’re mmm-mmm good.",
        "Is your dad an artist? Because you’re a masterpiece.",
        "Do you have a mirror in your pocket? Because I can see myself in your pants.",
        "Are you a bank loan? Because you’ve got my interest.",
        "Are you a parking ticket? Because you’ve got ‘FINE’ written all over you.",
        "If I were to ask you out, would your answer be the same as the answer to this question?",
        "Are you the ocean? Because I’m lost at sea.",
        "Can you lend me a kiss? I promise I’ll give it back.",
        "Is your name Waldo? Because someone like you is hard to find.",
        "Are you a photographer? Because I picture us together.",
        "Are you an electrician? Because you’re lighting up my life.",
        "Is your name Chapstick? Because you're da balm.",
        "You must be tired because you've been running through my mind all day.",
        "Can I follow you home? Cause my parents always told me to follow my dreams.",
        "Do you have a sunburn? Or are you always this hot?",
        "Are we at the airport? Because my heart is taking off.",
        "Do you like Star Wars? Because Yoda one for me.",
        "Are you a tower? Because Eiffel for you."
    ]

    # Select a random pickup line from the list
    selected_line = random.choice(pickup_lines)

    # Send the selected pickup line as a public message
    return f"One Line says: {selected_line}"

def HandleFortune():
    answers = [ 
        'Pass Go, Collect [̲̅$̲̅(̲̅ιοο̲̅)̲̅$̲̅] [̲̅$̲̅(̲̅ιοο̲̅)̲̅$̲̅] !',
        'When in anger, sing the alphabet.',
        'About time I got out of that cookie.',
        'Avoid taking unnecessary gambles. Lucky numbers: 2, 12, 10, 15, 6, 5.',
        'Ask your mom.',
        'I cannot help you; I am just a cookie.',
        'Ignore previous fortune cookies.',
        'Ignore future fortune cookies.',
        'The fortune you seek is in another cookie.',
        'Some fortune cookies contain no fortune.',
        'Always think something can go wrong, then you will always be right.',
        'Found the mistake in the code..',
        'Ask again later.',
        'If Hakuna Matata doesn’t work, then no worries.',
        'Maybe whoever has this will feel better? ~Matt~',
        'Tell x0r he’s pretty; it might save his life someday.',
        'Your future is bright, but you might need sunglasses.',
        'Happiness is a warm fortune cookie.',
        'The best way to predict your future is to create it.',
        'Expect great things to happen today.',
        'You will make someone very happy soon.',
        'Success is in your future. Keep going!',
        'Your hard work will soon pay off.',
        'A pleasant surprise is waiting for you.',
        'You are capable of amazing things.',
        'Good news will come to you by mail.',
        'You will overcome a major obstacle today.',
        'A new friendship will soon bring you joy.',
        'Opportunity is knocking; answer the door.',
        'Unexpected wealth is headed your way.',
        'Your kindness will lead to unexpected rewards.',
        'Today is a great day to start something new.',
        'A thrilling adventure is just around the corner.',
        'Believe in yourself, and others will too.',
        'Your creativity will soon be recognized.',
        'You will meet someone important soon.',
        'Trust your instincts; they are leading you in the right direction.',
        'A smile is your best accessory today.',
        'The answer you are seeking is on its way.',
        'Your perseverance will soon be rewarded.',
        'Good fortune will come to you in an unexpected way.',
        'A problem you’ve been struggling with will soon be solved.',
        'You are more powerful than you realize.',
        'Someone will soon make you an offer you can’t refuse.',
        'A dream you have will come true.',
        'You will soon receive a compliment that brightens your day.',
        'An unexpected event will bring you happiness.',
        'You will soon discover something you didn’t know you were good at.',
        'A small act of kindness will go a long way today.',
        'Adventure awaits you. Be bold and take the first step.',
        'The stars are aligning in your favor.',
        'You will soon find the answer to a lingering question.',
        'A positive attitude will lead you to success.',
        'A new opportunity is on the horizon.'
    ]

    # Select a random fortune from the list
    result = random.choice(answers)

    # Send the selected fortune as a public message
    return f"Fortune says: {result}"

def Handle8Ball():
    answers = [
        'It is certain',
        'It is decidedly so',
        'Without a doubt',
        'Yes definitely',
        'You may rely on it',
        'As I see it, yes',
        'Most likely',
        'Outlook good',
        'Yes',
        'Signs point to yes',
        'Signs point to no',
        'Don\'t count on it', 
        'My reply is no',
        'My sources say no',
        'Outlook not so good',
        'Very doubtful',
        'Why do you need to ask?',
        'Negative',
        'Indeed',
        'Sorry, that\'s not going to happen', 
        'Doubtful at best',
        'Don\'t take life too seriously',
        'Is Ed "Too Tall" Jones too tall?',
        'Does Charlie Daniels play a mean fiddle?',
        'Does Elmer Fudd have trouble with the letter R?',
        'Did The Waltons take way too long to say good night?',
        'Does a ten-pound bag of flour make a really big biscuit?',
        'Did the caveman invent fire?',
        'Was Abe Lincoln honest?',
        'Is having a snowball fight with pitching great Randy Johnson a bad idea?',
        'Is a bird in the hand worth two in the bush?',
        'Can fútbol announcer Andrés Cantor make any sport exciting?',
        'Does a former drill sergeant make a terrible therapist?',
        'Do woodchucks chuck wood?',
        'Did the little piggy really cry "wee wee wee" all the way home?',
        'Does it take two to tango?',
        'What, do you live under a rock?',
        'Does the buck stop here?',
        'Do dogs chase cats?',
        'Would Foghorn Leghorn make a really bad book narrator?',
        'Is the pen mightier than the sword?',
        'Do people use smartphones to do silly things?',
        'Would helium make opera sound less stuffy?',
        'Do mimes make even less sense when you can\'t see them?'
    ]

    question = "Ask a question and I’ll give you an answer!"  # Replace with actual question if available
    results = random.choice(answers)
    return f"8Ball says: {results}"
def HandleMood():

    moods = ['Happier than Gallagher at a Farmer\'s market.',
    'Happier than a Bodybuilder Directing Traffic.',
    'Happier than Christopher Columbus with Speedboats',
    'Happier than Eddie Money running a travel agency.',
    'Happier than a Witch at a Broom Factory',
    'Happier than a Slinky on an Escalator.',
    'Happier than an Antelope with Nightvision Goggles.',
    'Happier than Dikembe Mutombo Blocking a Shot.',
    'Happier than Paul Revere with a Cell phone.',
    'Happier than Dracula Volunteering at a Blood Drive.',
    'Happier than the Pillsbury Doughboy on his way to a Baking Convention.',
    'Happier than a Camel on Wednesday/Hump Day.']
    results = random.choice(moods)
    return f"Mood says: {results}"

def HandleGays():
    lines = [f'Two deers are walking out of a gay bar.One says to the other: /"I can’t believe I just blew 20 bucks in there!/"',
    'tst'
    'ree']
    return random.choice(lines)
def HandleAnimal():
    facts = [
        'The peacock mantis shrimp can throw a punch at 50 mph, accelerating quicker than a 22 caliber bullet.',
        'Studies have shown that wild chimps in Guinea drink fermented palm sap, which contains about 3 percent alcohol by volume.',
        'The chevrotain is an animal that looks like a tiny deer with fangs.',
        'Capuchin monkeys pee on their hands to wash their feet.',
        'Only the males are called peacocks. Females are called peahens.',
        'Dragonflies and damselflies form a heart with their tails when they mate.',
        'Baby elephants suck their trunks for comfort.',
        'Tigers have striped skin as well. Each pattern is as unique as a fingerprint.',
        'There was once a type of crocodile that could gallop.',
        'Sea otters hold hands while they\'re sleeping so they don\'t drift apart.',
        'Prairie dogs say hello by kissing.',
        'Animal behaviorists have concluded that cats don’t meow as a way to communicate with each other. It’s a method they use for getting attention from humans.',
        'Despite their appearance, elephant shrews are more closely related to elephants than shrews.',
        'Flamingos are naturally white—their diet of brine shrimp and algae turns them pink.',
        'Alberta, Canada is the largest rat-free populated area in the world.',
        'Red-eyed tree frog eggs can hatch early if they sense danger.',
        'Whitetail deer can sprint at speeds up to 30 miles per hour.',
        'Blue jays mimic hawk calls to scare away other birds.',
        'In the UK, the British monarch legally owns all unmarked mute swans in open water.',
        'All clownfish are born male—some turn female to enable mating.',
        'Moray eels have a second set of jaws that extends from their throats.',
        'Male ring-tailed lemurs will "stink fight" by wafting scent at each other.',
        'Octopuses have three hearts and blue blood.',
        'A group of flamingos is called a "flamboyance."',
        'Horses can sleep both lying down and standing up.',
        'Giraffes have the same number of neck vertebrae as humans: seven.',
        'Kangaroos can’t walk backward.',
        'The heart of a shrimp is located in its head.',
        'Honeybees can recognize human faces.',
        'Elephants are the only animals that can’t jump.',
        'A cheetah’s claws are not retractable, unlike other cats.',
        'The largest recorded snowflake was 15 inches wide.',
        'Butterflies taste with their feet.',
        'Sloths only defecate once a week.',
        'The shortest war in history was between Britain and Zanzibar. Zanzibar surrendered after 38 minutes.',
        'Starfish can regenerate lost arms, and some can grow an entire new body from a single arm.',
        'Penguins propose to their mates with a pebble.',
        'A newborn kangaroo is the size of a lima bean.',
        'Elephant seals can hold their breath for up to two hours.',
        'A group of owls is called a "parliament."',
        'Dolphins have names for each other.',
        'Wombat feces are cube-shaped.',
        'Sea horses are the only animals where the male gets pregnant.',
        'A rabbit’s teeth never stop growing.',
        'The average cow produces around 6.3 gallons of milk each day.',
        'Pandas spend up to 14 hours a day eating bamboo.',
        'A group of crows is called a "murder."',
        'Male seahorses give birth, not females.',
        'Tardigrades, also known as water bears, can survive in space.',
        'There are more than 1,000 different species of bats.',
        'A blue whale’s heart is the size of a small car.',
        'The cheetah is the fastest land animal, capable of running 60 to 70 miles per hour.',
        'The longest-lived mammal in the world is the bowhead whale, which can live over 200 years.',
        'A giraffe’s tongue is blue-black to protect it from sunburn.',
        'The elephant’s trunk has about 150,000 muscle units.',
        'A group of flamingos is called a "flamboyance."',
        'Bees have been around for 30 million years.',
        'An adult lion’s roar can be heard up to 5 miles away.',
        'Hummingbirds are the only birds that can fly backward.',
        'A leopard’s spots are unique, like human fingerprints.',
        'Ostriches’ eyes are larger than their brains.'
    ]

    # Select a random fact from the list
    result = random.choice(facts)

    # Return the selected fact
    return f"Animal Fact: {result}"

def HandleDadJoke():
    jokes = [
        'Why don’t skeletons fight each other? They don’t have the guts.',
        'What do you call fake spaghetti? An impasta.',
        'How does a penguin build its house? Igloos it together.',
        'Why don’t some couples go to the gym? Because some relationships don’t work out.',
        'What do you call cheese that isn’t yours? Nacho cheese.',
        'How does a scientist freshen her breath? With experi-mints.',
        'Why did the scarecrow win an award? Because he was outstanding in his field.',
        'What do you call an alligator in a vest? An investigator.',
        'Why don’t eggs tell jokes? They’d crack each other up.',
        'What do you call a factory that makes good products? A satisfactory.',
        'Why did the math book look sad? Because it had too many problems.',
        'How does a snowman get around? By riding an "icicle."',
        'What did one plate say to the other plate? Lunch is on me.',
        'Why did the golfer bring two pairs of pants? In case he got a hole in one.',
        'What do you call a bear with no teeth? A gummy bear.',
        'Why did the bicycle fall over? It was two-tired.',
        'What did the janitor say when he jumped out of the closet? Supplies!',
        'How do you organize a space party? You planet.',
        'Why did the chicken go to the seance? To talk to the other side.',
        'What do you call a fish wearing a bowtie? Sofishticated.',
        'Why did the computer go to the doctor? Because it had a virus.',
        'What did the grape do when he got stepped on? Nothing but let out a little wine.',
        'Why do cows wear bells? Because their horns don’t work.',
        'What did the ocean say to the beach? Nothing, it just waved.',
        'Why don’t some people get sunburned? Because they have sunscreen.',
        'What do you call a pile of cats? A meowtain.',
        'What’s brown and sticky? A stick.',
        'How does a duck walk? With its quack.',
        'Why did the math teacher break up with the calculator? It couldn’t solve its problems.',
        'What’s orange and sounds like a parrot? A carrot.',
        'Why did the scarecrow become a successful neurosurgeon? Because he was outstanding in his field.',
        'How does a vampire start a letter? "Tomb it may concern..."',
        'What do you call a dinosaur with an extensive vocabulary? A thesaurus.',
        'What’s green and has wheels? Grass, I lied about the wheels.',
        'Why did the coffee file a police report? It got mugged.',
        'What did the big flower say to the little flower? "Hey, bud!"',
        'Why did the tomato turn red? Because it saw the salad dressing.',
        'What did one hat say to the other? "You stay here, I’ll go on ahead!"',
        'Why don’t scientists trust atoms? Because they make up everything.',
        'How do you make a tissue dance? You put a little boogie in it.',
        'What do you call a snowman with a six-pack? An abdominal snowman.',
        'Why did the belt go to jail? For holding up a pair of pants.',
        'What do you call a lazy kangaroo? A pouch potato.',
        'What do you get when you cross a snowman and a vampire? Frostbite.',
        'Why did the bicycle fall over? Because it was two-tired.',
        'How do you catch a squirrel? Climb a tree and act like a nut.',
        'What did the duck say when it bought lipstick? "Put it on my bill."',
        'What do you call a fish without eyes? Fsh.',
        'Why did the golfer bring extra socks? In case he got a hole in one.',
        'What’s a skeleton’s least favorite room in the house? The living room.',
        'Why don’t skeletons fight each other? They don’t have the guts.',
        'What did the janitor say when he jumped out of the closet? "Supplies!"',
        'What do you call a boomerang that doesn’t come back? A stick.'
    ]

    # Select a random dad joke from the list
    result = random.choice(jokes)

    # Return the selected joke
    return f"Dad Joke: {result}"

### Youtube ###

def search_imgur(query):
    # Define the endpoint URL and headers for the Imgur API request
    url = 'https://api.imgur.com/3/gallery/search/'
    headers = {
        'Authorization': f'Client-ID 296a3dbe2ba7e78'
    }
    params = {
        'q': query,
        'q_type': 'png'  # Optional: Filter by image type
    }

    try:
        # Make the API request
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON response
        data = response.json()

        if data['data']:
            # Get the link of the first image
            first_image = data['data'][0]
            if 'link' in first_image:
                return first_image['link']
            else:
                return 'No image link found in the results.'
        else:
            return 'No results found.'

    except requests.RequestException as e:
        return f'Error: {str(e)}'

def get_excuse():
    excuses = [
        "My dog ate my homework!",
        "I was abducted by aliens and lost track of time.",
        "I accidentally locked myself in the bathroom.",
        "My alarm clock thought it was a weekend.",
        "A squirrel stole my keys and I had to negotiate to get them back.",
        "I slipped on a banana peel in my kitchen.",
        "My car turned into a pumpkin at midnight.",
        "I was busy battling my inner demons and they won.",
        "The Wi-Fi was down, and I had to resort to carrier pigeons.",
        "I couldn't find my glasses because I was looking without them.",
        "I tripped over my cat on the way out.",
        "I was perfecting my time travel machine and lost track of time.",
        "A pigeon stole my phone, so I couldn't call.",
        "I was in a staring contest with my reflection and lost.",
        "I was trying to understand quantum physics and forgot everything else.",
        "I got my days mixed up because I live in a time loop.",
        "The traffic lights were only green for milliseconds today.",
        "I was busy training my hamster for the Olympics.",
        "My imaginary friend was throwing a surprise party for me.",
        "I mistook my phone for a toaster and now it’s gone.",
        "My house got trapped in a snow globe!",
        "I lost a battle with my blanket this morning.",
        "I was on a mission to save a village in my dream.",
        "A ninja swapped all my clocks with chocolate ones.",
        "My psychic told me I needed to rest today.",
        "A cloud followed me everywhere and rained only on me.",
        "The sun was too bright, and I couldn’t see my way here.",
        "I had a wrestling match with my alarm clock and it won.",
        "I tried to solve world hunger and lost track of time.",
        "My spirit animal needed a pep talk today.",
        "I was writing a novel in my head and got carried away.",
        "I joined a snail race and we’re still halfway.",
        "My lucky socks were missing; I couldn’t risk it.",
        "My goldfish turned on the TV, and I was mesmerized.",
        "I had to finish a Sudoku or the world would end.",
        "The post office kidnapped my schedule.",
        "I was translating whale sounds and got caught up.",
        "A riddle from a stranger on the subway occupied my mind.",
        "My house ran away, so I had to chase it down.",
        "My plants staged a protest for water and won.",
        "I got caught in a conspiracy theory rabbit hole online.",
        "My shadow refused to follow me out today.",
        "A wizard put a spell on my front door.",
        "I went to take out the trash and found a secret passage.",
        "My pillow held me captive in bed.",
        "A dragon blocked my way and demanded a password.",
        "The stars told me to stay put.",
        "I lost my map and wandered to the wrong dimension.",
        "The line at the coffee shop was moving backward.",
        "The moon told me it was daytime and I got confused.",
        "I forgot the world is round and took the long way."
    ]
    return random.choice(excuses)
