from myapp.models import QuizQuestion

def load_initial_data():
    # Check if there are no quiz questions in the database
    if not QuizQuestion.objects.exists():
        # Create some default quiz questions
        QuizQuestion.objects.create(
            question="What is the capital of France?",
            options=['Berlin', 'London', 'Paris'],
            correct_option='Paris'
        )
        QuizQuestion.objects.create(
            question="Who wrote 'Romeo and Juliet'?",
            options=['Charles Dickens', 'William Shakespeare', 'Jane Austen'],
            correct_option='William Shakespeare'
        )
        QuizQuestion.objects.create(
            question="What is the largest planet in our solar system?",
            options=['Earth', 'Jupiter', 'Mars'],
            correct_option='Jupiter'
        )
        QuizQuestion.objects.create(
            question="In which year did World War II end?",
            options=['1945', '1918', '1939'],
            correct_option='1945'
        )
        QuizQuestion.objects.create(
            question="What is the capital of Japan?",
            options=['Beijing', 'Seoul', 'Tokyo'],
            correct_option='Tokyo'
        )
        QuizQuestion.objects.create(
            question="Who painted the Mona Lisa?",
            options=['Vincent van Gogh', 'Leonardo da Vinci', 'Pablo Picasso'],
            correct_option='Leonardo da Vinci'
        )
        QuizQuestion.objects.create(
            question="What is the chemical symbol for gold?",
            options=['Au', 'Ag', 'Fe'],
            correct_option='Au'
        )
        QuizQuestion.objects.create(
            question="Which planet is known as the 'Red Planet'?",
            options=['Mars', 'Venus', 'Jupiter'],
            correct_option='Mars'
        )
        QuizQuestion.objects.create(
            question="Who was the first President of the United States?",
            options=['Thomas Jefferson', 'George Washington', 'Abraham Lincoln'],
            correct_option='George Washington'
        )
        QuizQuestion.objects.create(
            question="In which continent is the Sahara Desert located?",
            options=['Asia', 'Africa', 'South America'],
            correct_option='Africa'
        )
        QuizQuestion.objects.create(
            question="What is the square root of 144?",
            options=['10', '12', '14'],
            correct_option='12'
        )
        QuizQuestion.objects.create(
            question="Who wrote 'To Kill a Mockingbird'?",
            options=['J.K. Rowling', 'Harper Lee', 'George Orwell'],
            correct_option='Harper Lee'
        )
        QuizQuestion.objects.create(
            question="What is the capital of Australia?",
            options=['Sydney', 'Canberra', 'Melbourne'],
            correct_option='Canberra'
        )
        QuizQuestion.objects.create(
            question="Which element has the chemical symbol 'O'?",
            options=['Oxygen', 'Osmium', 'Gold'],
            correct_option='Oxygen'
        )
        QuizQuestion.objects.create(
            question="Who developed the theory of relativity?",
            options=['Isaac Newton', 'Albert Einstein', 'Galileo Galilei'],
            correct_option='Albert Einstein'
        )
        QuizQuestion.objects.create(
            question="What is the currency of China?",
            options=['Yen', 'Won', 'Yuan'],
            correct_option='Yuan'
        )
        QuizQuestion.objects.create(
            question="In which year did the Titanic sink?",
            options=['1912', '1920', '1905'],
            correct_option='1912'
        )
        QuizQuestion.objects.create(
            question="What is the largest ocean on Earth?",
            options=['Indian Ocean', 'Atlantic Ocean', 'Pacific Ocean'],
            correct_option='Pacific Ocean'
        )
        QuizQuestion.objects.create(
            question="Who wrote '1984'?",
            options=['George Orwell', 'Aldous Huxley', 'Ray Bradbury'],
            correct_option='George Orwell'
        )
        QuizQuestion.objects.create(
            question="What is the main component of Earth's atmosphere?",
            options=['Nitrogen', 'Oxygen', 'Carbon Dioxide'],
            correct_option='Oxygen'
        )
        QuizQuestion.objects.create(
            question="What is the primary gas responsible for the greenhouse effect?",
            options=['Oxygen', 'Carbon Dioxide', 'Nitrogen', 'Methane'],
            correct_option='Carbon Dioxide'
        )
        QuizQuestion.objects.create(
            question="Which of the following is a renewable energy source?",
            options=['Coal', 'Natural Gas', 'Solar', 'Oil'],
            correct_option='Solar'
        )
        QuizQuestion.objects.create(
            question="What is the largest source of ocean pollution?",
            options=['Plastic', 'Oil spills', 'Industrial runoff', 'Sewage'],
            correct_option='Plastic'
        )
        QuizQuestion.objects.create(
            question="Which organization is known for its efforts in wildlife conservation?",
            options=['Greenpeace', 'NASA', 'WHO', 'UNESCO'],
            correct_option='Greenpeace'
        )
        QuizQuestion.objects.create(
            question="What is the term for the loss of a species from a particular habitat or from the entire planet?",
            options=['Extinction', 'Migration', 'Hibernation', 'Speciation'],
            correct_option='Extinction'
        )
        QuizQuestion.objects.create(
            question="What is the main cause of deforestation?",
            options=['Urbanization', 'Logging', 'Agriculture', 'Mining'],
            correct_option='Agriculture'
        )
        QuizQuestion.objects.create(
            question="Which gas is responsible for the thinning of the ozone layer?",
            options=['Carbon Dioxide', 'Methane', 'Chlorofluorocarbons (CFCs)', 'Nitrous Oxide'],
            correct_option='Chlorofluorocarbons (CFCs)'
        )
        QuizQuestion.objects.create(
            question="What is the term for the gradual increase in the Earth's average temperature?",
            options=['Global Cooling', 'Greenhouse Effect', 'Ozone Depletion', 'Global Warming'],
            correct_option='Global Warming'
        )
        QuizQuestion.objects.create(
            question="Which ocean is the largest and deepest?",
            options=['Atlantic Ocean', 'Indian Ocean', 'Southern Ocean', 'Pacific Ocean'],
            correct_option='Pacific Ocean'
        )
        QuizQuestion.objects.create(
            question="What is the purpose of a wildlife corridor?",
            options=['To protect against wildfires', 'To provide a route for wildlife migration', 'To prevent soil erosion', 'To store carbon dioxide'],
            correct_option='To provide a route for wildlife migration'
        )
        QuizQuestion.objects.create(
            question="What is the main component of smog in urban areas?",
            options=['Oxygen', 'Nitrogen', 'Sulfur Dioxide', 'Carbon Monoxide'],
            correct_option='Sulfur Dioxide'
        )
        QuizQuestion.objects.create(
            question="Which of the following is a non-renewable resource?",
            options=['Wind', 'Coal', 'Solar', 'Geothermal'],
            correct_option='Coal'
        )
        QuizQuestion.objects.create(
            question="What is the term for the practice of planting trees to restore or create a forest?",
            options=['Afforestation', 'Reforestation', 'Deforestation', 'Desertification'],
            correct_option='Reforestation'
        )
        QuizQuestion.objects.create(
            question="What is the main cause of ocean acidification?",
            options=['Deforestation', 'Industrial pollution', 'Greenhouse gas emissions', 'Oil spills'],
            correct_option='Greenhouse gas emissions'
        )
        QuizQuestion.objects.create(
            question="Which environmental treaty aims to protect the ozone layer?",
            options=['Kyoto Protocol', 'Paris Agreement', 'Montreal Protocol', 'Basel Convention'],
            correct_option='Montreal Protocol'
        )
        QuizQuestion.objects.create(
            question="What is the term for the process by which plants make their own food using sunlight?",
            options=['Respiration', 'Photosynthesis', 'Transpiration', 'Germination'],
            correct_option='Photosynthesis'
        )
        QuizQuestion.objects.create(
            question="Which of the following is a renewable source of freshwater?",
            options=['Groundwater', 'Saltwater', 'Ice caps and glaciers', 'Seawater'],
            correct_option='Groundwater'
        )
        QuizQuestion.objects.create(
            question="What is the main cause of coral reef bleaching?",
            options=['Ocean acidification', 'Overfishing', 'Pollution', 'Rising sea temperatures'],
            correct_option='Rising sea temperatures'
        )
        QuizQuestion.objects.create(
            question="What is the term for the process of converting waste materials into reusable materials?",
            options=['Recycling', 'Incineration', 'Landfilling', 'Composting'],
            correct_option='Recycling'
        )
        QuizQuestion.objects.create(
            question="Which endangered species is known for its distinctive black and white fur?",
            options=['Bengal Tiger', 'Giant Panda', 'African Elephant', 'Leatherback Turtle'],
            correct_option='Giant Panda'
        )
        QuizQuestion.objects.create(
            question="What is the largest mammal on Earth?",
            options=['Elephant', 'Blue Whale', 'Giraffe'],
            correct_option='Blue Whale'
        )
        QuizQuestion.objects.create(
            question="Which bird is known for its ability to mimic human speech?",
            options=['Penguin', 'Parrot', 'Eagle'],
            correct_option='Parrot'
        )
        QuizQuestion.objects.create(
            question="What is the largest species of lizard?",
            options=['Iguana', 'Komodo Dragon', 'Chameleon'],
            correct_option='Komodo Dragon'
        )
        QuizQuestion.objects.create(
            question="Which amphibian is known for its ability to change color?",
            options=['Salamander', 'Frog', 'Toad'],
            correct_option='Salamander'
        )
        QuizQuestion.objects.create(
            question="Which fish is famous for its electric shocks?",
            options=['Clownfish', 'Electric Eel', 'Salmon'],
            correct_option='Electric Eel'
        )
        QuizQuestion.objects.create(
            question="What is the largest species of butterfly?",
            options=['Monarch Butterfly', 'Swallowtail Butterfly', 'Atlas Moth'],
            correct_option='Atlas Moth'
        )
        QuizQuestion.objects.create(
            question="Which mammal carries its young in a pouch?",
            options=['Kangaroo', 'Koala', 'Tasmanian Devil'],
            correct_option='Kangaroo'
        )
        QuizQuestion.objects.create(
            question="What is the primary food source for polar bears?",
            options=['Fish', 'Seals', 'Penguins'],
            correct_option='Seals'
        )
        QuizQuestion.objects.create(
            question="Which big cat is critically endangered?",
            options=['Tiger', 'Lion', 'Snow Leopard'],
            correct_option='Snow Leopard'
        )
        QuizQuestion.objects.create(
            question="What is the largest species of shark?",
            options=['Great White Shark', 'Hammerhead Shark', 'Whale Shark'],
            correct_option='Whale Shark'
        )
        QuizQuestion.objects.create(
            question="What is the most popular pet fish?",
            options=['Goldfish', 'Betta Fish', 'Guppy'],
            correct_option='Goldfish'
        )
        QuizQuestion.objects.create(
            question="Which large herbivorous mammal has a trunk?",
            options=['Rhino', 'Elephant', 'Hippopotamus'],
            correct_option='Elephant'
        )
        QuizQuestion.objects.create(
            question="What is the largest known dinosaur?",
            options=['Tyrannosaurus Rex', 'Triceratops', 'Brachiosaurus'],
            correct_option='Brachiosaurus'
        )
        QuizQuestion.objects.create(
            question="Which animal is known for its ability to rotate its head up to 270 degrees?",
            options=['Owl', 'Bat', 'Lemur'],
            correct_option='Owl'
        )
        QuizQuestion.objects.create(
            question="What is the largest primate in the world?",
            options=['Chimpanzee', 'Gorilla', 'Orangutan'],
            correct_option='Gorilla'
        )
        QuizQuestion.objects.create(
            question="Which marsupial is native to Australia and known for carrying its young in a pouch?",
            options=['Wallaby', 'Quokka', 'Koala'],
            correct_option='Koala'
        )
        QuizQuestion.objects.create(
            question="Which bird is known for its long annual migration from the Arctic to the Antarctic?",
            options=['Puffin', 'Albatross', 'Arctic Tern'],
            correct_option='Arctic Tern'
        )
        QuizQuestion.objects.create(
            question="Which large herbivore is native to the African savannah and known for its distinctive horns?",
            options=['Buffalo', 'Gazelle', 'Wildebeest'],
            correct_option='Wildebeest'
        )
        QuizQuestion.objects.create(
            question="What is the primary function of a camel's hump?",
            options=['Water storage', 'Fat storage', 'Temperature regulation'],
            correct_option='Fat storage'
        )
        QuizQuestion.objects.create(
            question="Which sea creature is known for its bioluminescence, producing light in the dark ocean depths?",
            options=['Jellyfish', 'Squid', 'Anglerfish'],
            correct_option='Anglerfish'
        )
        QuizQuestion.objects.create(
            question="Which sea creature is known for its bioluminescence, producing light in the dark ocean depths?",
            options=['Jellyfish', 'Squid', 'Anglerfish'],
            correct_option='Anglerfish'
        )
        QuizQuestion.objects.create(
            question="What is the capital of France?",
            options=['Berlin', 'Paris', 'Rome'],
            correct_option='Paris'
        )
        QuizQuestion.objects.create(
            question="Which river is the longest in the world?",
            options=['Amazon', 'Nile', 'Mississippi'],
            correct_option='Nile'
        )
        QuizQuestion.objects.create(
            question="In which continent is the Sahara Desert located?",
            options=['Asia', 'Africa', 'South America'],
            correct_option='Africa'
        )
        QuizQuestion.objects.create(
            question="What is the largest ocean on Earth?",
            options=['Indian Ocean', 'Atlantic Ocean', 'Pacific Ocean'],
            correct_option='Pacific Ocean'
        )
        QuizQuestion.objects.create(
            question="Which mountain range spans across seven countries, including India and Nepal?",
            options=['Rocky Mountains', 'Alps', 'Himalayas'],
            correct_option='Himalayas'
        )
        QuizQuestion.objects.create(
            question="What is the capital of Canada?",
            options=['Ottawa', 'Toronto', 'Vancouver'],
            correct_option='Ottawa'
        )
        QuizQuestion.objects.create(
            question="Which country is known as the Land of the Rising Sun?",
            options=['China', 'Japan', 'South Korea'],
            correct_option='Japan'
        )
        QuizQuestion.objects.create(
            question="The Great Barrier Reef is located off the coast of which country?",
            options=['Brazil', 'Australia', 'Mexico'],
            correct_option='Australia'
        )
        QuizQuestion.objects.create(
            question="What is the capital of South Africa?",
            options=['Nairobi', 'Cairo', 'Pretoria'],
            correct_option='Pretoria'
        )
        QuizQuestion.objects.create(
            question="Which of the following is the largest island in the world?",
            options=['Greenland', 'Borneo', 'Iceland'],
            correct_option='Greenland'
        )
        QuizQuestion.objects.create(
            question="What is the currency of Japan?",
            options=['Yen', 'Won', 'Ringgit'],
            correct_option='Yen'
        )
        QuizQuestion.objects.create(
            question="The Panama Canal connects which two oceans?",
            options=['Atlantic and Indian Ocean', 'Pacific and Arctic Ocean', 'Atlantic and Pacific Ocean'],
            correct_option='Atlantic and Pacific Ocean'
        )
        QuizQuestion.objects.create(
            question="Which desert is often called the 'Outback' and is located in Australia?",
            options=['Mojave Desert', 'Gobi Desert', 'Great Victoria Desert'],
            correct_option='Great Victoria Desert'
        )
        QuizQuestion.objects.create(
            question="What is the official language of Brazil?",
            options=['Spanish', 'Portuguese', 'French'],
            correct_option='Portuguese'
        )
        QuizQuestion.objects.create(
            question="In which country would you find the famous city of Istanbul?",
            options=['Greece', 'Turkey', 'Egypt'],
            correct_option='Turkey'
        )
        QuizQuestion.objects.create(
            question="The Amazon Rainforest is primarily located in which country?",
            options=['Brazil', 'Colombia', 'Peru'],
            correct_option='Brazil'
        )
        QuizQuestion.objects.create(
            question="Which river is associated with the ancient civilization of Mesopotamia?",
            options=['Tigris', 'Nile', 'Euphrates'],
            correct_option='Euphrates'
        )
        QuizQuestion.objects.create(
            question="The city of Marrakech is located in which African country?",
            options=['Egypt', 'Morocco', 'Nigeria'],
            correct_option='Morocco'
        )
        QuizQuestion.objects.create(
            question="What is the highest mountain in North America?",
            options=['Denali (Mount McKinley)', 'Mount Elbert', 'Mount Logan'],
            correct_option='Denali (Mount McKinley)'
        )
        QuizQuestion.objects.create(
            question="Which European country is known as the 'Land of a Thousand Lakes'?",
            options=['Finland', 'Sweden', 'Norway'],
            correct_option='Finland'
        )

        # Additional Questions - Part 4
        QuizQuestion.objects.create(
            question="What is the chemical symbol for gold?",
            options=['Go', 'Au', 'Ag'],
            correct_option='Au'
        )
        QuizQuestion.objects.create(
            question="Which planet is known as the 'Red Planet'?",
            options=['Venus', 'Mars', 'Jupiter'],
            correct_option='Mars'
        )
        QuizQuestion.objects.create(
            question="What is the powerhouse of the cell?",
            options=['Nucleus', 'Mitochondria', 'Endoplasmic reticulum'],
            correct_option='Mitochondria'
        )
        QuizQuestion.objects.create(
            question="Who developed the theory of relativity?",
            options=['Isaac Newton', 'Albert Einstein', 'Galileo Galilei'],
            correct_option='Albert Einstein'
        )
        QuizQuestion.objects.create(
            question="What is the largest organ in the human body?",
            options=['Liver', 'Skin', 'Heart'],
            correct_option='Skin'
        )
        QuizQuestion.objects.create(
            question="Which gas do plants absorb from the atmosphere during photosynthesis?",
            options=['Oxygen', 'Carbon dioxide', 'Nitrogen'],
            correct_option='Carbon dioxide'
        )
        QuizQuestion.objects.create(
            question="What is the chemical symbol for water?",
            options=['Wo', 'Wa', 'H2O'],
            correct_option='H2O'
        )
        QuizQuestion.objects.create(
            question="What is the speed of light in a vacuum?",
            options=['300,000 km/s', '150,000 km/s', '500,000 km/s'],
            correct_option='300,000 km/s'
        )
        QuizQuestion.objects.create(
            question="Who discovered penicillin?",
            options=['Alexander Fleming', 'Louis Pasteur', 'Marie Curie'],
            correct_option='Alexander Fleming'
        )
        QuizQuestion.objects.create(
            question="What is the smallest prime number?",
            options=['0', '1', '2'],
            correct_option='2'
        )
        QuizQuestion.objects.create(
            question="What is the chemical formula for table salt?",
            options=['NaCl', 'HCl', 'KCl'],
            correct_option='NaCl'
        )
        QuizQuestion.objects.create(
            question="Which gas do plants release during photosynthesis?",
            options=['Oxygen', 'Carbon dioxide', 'Nitrous oxide'],
            correct_option='Oxygen'
        )
        QuizQuestion.objects.create(
            question="What is the main function of the ozone layer?",
            options=['Trap heat', 'Block ultraviolet radiation', 'Generate electricity'],
            correct_option='Block ultraviolet radiation'
        )
        QuizQuestion.objects.create(
            question="Who is known as the father of modern physics?",
            options=['Isaac Newton', 'Galileo Galilei', 'Albert Einstein'],
            correct_option='Albert Einstein'
        )
        QuizQuestion.objects.create(
            question="What is the chemical symbol for iron?",
            options=['Ir', 'Fe', 'In'],
            correct_option='Fe'
        )
        QuizQuestion.objects.create(
            question="What is the largest ocean on Earth?",
            options=['Indian Ocean', 'Atlantic Ocean', 'Pacific Ocean'],
            correct_option='Pacific Ocean'
        )
        QuizQuestion.objects.create(
            question="Which gas makes up the majority of Earth's atmosphere?",
            options=['Oxygen', 'Nitrogen', 'Carbon dioxide'],
            correct_option='Nitrogen'
        )
        QuizQuestion.objects.create(
            question="What is the process by which plants make their own food?",
            options=['Respiration', 'Photosynthesis', 'Transpiration'],
            correct_option='Photosynthesis'
        )
        QuizQuestion.objects.create(
            question="Who proposed the heliocentric model of the solar system?",
            options=['Ptolemy', 'Copernicus', 'Kepler'],
            correct_option='Copernicus'
        )
        QuizQuestion.objects.create(
            question="What is the unit of electric current?",
            options=['Watt', 'Volt', 'Ampere'],
            correct_option='Ampere'
        )
        QuizQuestion.objects.create(
            question="What is the value of π (pi)?",
            options=['2.718', '3.142', '1.618'],
            correct_option='3.142'
        )
        QuizQuestion.objects.create(
            question="In a right-angled triangle, which side is opposite the right angle?",
            options=['Hypotenuse', 'Adjacent', 'Opposite'],
            correct_option='Hypotenuse'
        )
        QuizQuestion.objects.create(
            question="What is the result of multiplying any number by zero?",
            options=['1', '0', 'Infinity'],
            correct_option='0'
        )
        QuizQuestion.objects.create(
            question="Which of the following is a prime number?",
            options=['1', '8', '17'],
            correct_option='17'
        )
        QuizQuestion.objects.create(
            question="What is the sum of the angles in a triangle?",
            options=['90 degrees', '180 degrees', '360 degrees'],
            correct_option='180 degrees'
        )
        QuizQuestion.objects.create(
            question="What is the square root of 64?",
            options=['6', '8', '10'],
            correct_option='8'
        )
        QuizQuestion.objects.create(
            question="In geometry, what do we call a polygon with eight sides?",
            options=['Hexagon', 'Octagon', 'Decagon'],
            correct_option='Octagon'
        )
        QuizQuestion.objects.create(
            question="If a rectangle has a length of 5 units and a width of 8 units, what is its area?",
            options=['13 sq units', '40 sq units', '64 sq units'],
            correct_option='64 sq units'
        )
        QuizQuestion.objects.create(
            question="What is the value of 2 to the power of 3?",
            options=['6', '8', '16'],
            correct_option='8'
        )
        QuizQuestion.objects.create(
            question="What is the circumference formula of a circle?",
            options=['πr²', '2πr', 'πd'],
            correct_option='2πr'
        )
        QuizQuestion.objects.create(
            question="What is the formula for the area of a triangle?",
            options=['0.5bh', 'l²', 'πr²'],
            correct_option='0.5bh'
        )
        QuizQuestion.objects.create(
            question="Which trigonometric function is equal to the ratio of the opposite side to the hypotenuse in a right-angled triangle?",
            options=['Sine', 'Cosine', 'Tangent'],
            correct_option='Sine'
        )
        QuizQuestion.objects.create(
            question="How many degrees are in a full circle?",
            options=['180', '270', '360'],
            correct_option='360'
        )
        QuizQuestion.objects.create(
            question="What is the value of the mathematical constant 'e' approximately equal to?",
            options=['2.718', '3.142', '1.618'],
            correct_option='2.718'
        )
        QuizQuestion.objects.create(
            question="What is the sum of the interior angles of a hexagon?",
            options=['90 degrees', '120 degrees', '720 degrees'],
            correct_option='720 degrees'
        )
        QuizQuestion.objects.create(
            question="Which of the following is not a type of triangle?",
            options=['Equilateral', 'Isosceles', 'Quadrilateral'],
            correct_option='Quadrilateral'
        )
        QuizQuestion.objects.create(
            question="What is the value of 10 factorial (10!)?",
            options=['45', '362,880', '100'],
            correct_option='362,880'
        )
        QuizQuestion.objects.create(
            question="What is the Pythagorean theorem?",
            options=['a² + b² = c²', 'πr²', '2πr'],
            correct_option='a² + b² = c²'
        )
        QuizQuestion.objects.create(
            question="If x + 5 = 10, what is the value of x?",
            options=['5', '10', '15'],
            correct_option='5'
        )
        QuizQuestion.objects.create(
            question="What is the decimal equivalent of the fraction 3/4?",
            options=['0.25', '0.5', '0.75'],
            correct_option='0.75'
        )
        QuizQuestion.objects.create(
            question="Who is considered the national hero of the Philippines?",
            options=['Jose Rizal', 'Andres Bonifacio', 'Emilio Aguinaldo'],
            correct_option='Jose Rizal'
        )
        QuizQuestion.objects.create(
            question="When did the Philippines gain independence from Spanish rule?",
            options=['1896', '1898', '1901'],
            correct_option='1898'
        )
        QuizQuestion.objects.create(
            question="Which battle marked the end of Spanish colonization in the Philippines?",
            options=['Battle of Mactan', 'Battle of Manila Bay', 'Battle of Bataan'],
            correct_option='Battle of Manila Bay'
        )
        QuizQuestion.objects.create(
            question="Who declared the independence of the Philippines on June 12, 1898?",
            options=['Andres Bonifacio', 'Emilio Aguinaldo', 'Apolinario Mabini'],
            correct_option='Emilio Aguinaldo'
        )
        QuizQuestion.objects.create(
            question="What event led to the Philippines becoming a colony of the United States in 1899?",
            options=['Treaty of Paris', 'Treaty of Tordesillas', 'Treaty of Versailles'],
            correct_option='Treaty of Paris'
        )
        QuizQuestion.objects.create(
            question="During World War II, which country occupied the Philippines?",
            options=['Japan', 'Germany', 'Italy'],
            correct_option='Japan'
        )
        QuizQuestion.objects.create(
            question="Where did General Douglas MacArthur fulfill his famous promise 'I shall return' during World War II?",
            options=['Corregidor', 'Leyte', 'Bataan'],
            correct_option='Leyte'
        )
        QuizQuestion.objects.create(
            question="What is the name of the underground resistance movement during the Japanese occupation?",
            options=['Katipunan', 'Hukbalahap', 'KALIBAPI'],
            correct_option='Hukbalahap'
        )
        QuizQuestion.objects.create(
            question="Which president declared martial law in the Philippines in 1972?",
            options=['Ferdinand Marcos', 'Corazon Aquino', 'Gloria Macapagal-Arroyo'],
            correct_option='Ferdinand Marcos'
        )
        QuizQuestion.objects.create(
            question="What event marked the end of the martial law era in the Philippines?",
            options=['People Power Revolution', 'EDSA Revolution', 'Cry of Pugad Lawin'],
            correct_option='EDSA Revolution'
        )
        QuizQuestion.objects.create(
            question="Who became the first female president of the Philippines?",
            options=['Gloria Macapagal-Arroyo', 'Imelda Marcos', 'Corazon Aquino'],
            correct_option='Corazon Aquino'
        )
        QuizQuestion.objects.create(
            question="In what year did the eruption of Mount Pinatubo significantly impact the Philippines?",
            options=['1989', '1991', '1993'],
            correct_option='1991'
        )
        QuizQuestion.objects.create(
            question="Which city served as the temporary capital of the Philippines during World War II?",
            options=['Baguio', 'Cebu', 'Davao'],
            correct_option='Baguio'
        )
        QuizQuestion.objects.create(
            question="What is the official language of the Philippines?",
            options=['English', 'Tagalog', 'Filipino'],
            correct_option='Filipino'
        )
        QuizQuestion.objects.create(
            question="Which Philippine president is known for the 'Economic Miracle' during the 1960s?",
            options=['Diosdado Macapagal', 'Ferdinand Marcos', 'Ramon Magsaysay'],
            correct_option='Diosdado Macapagal'
        )
        QuizQuestion.objects.create(
            question="What is the name of the historic document proclaiming Philippine independence in 1898?",
            options=['Declaration of Independence', 'Malolos Constitution', 'Pact of Biak-na-Bato'],
            correct_option='Malolos Constitution'
        )
        QuizQuestion.objects.create(
            question="Which group fought for Philippine independence against both Spanish and American rule?",
            options=['Katipunan', 'Huks', 'Sakdalistas'],
            correct_option='Katipunan'
        )
        QuizQuestion.objects.create(
            question="Who was the first Filipino to circumnavigate the world?",
            options=['Ferdinand Magellan', 'Lapu-Lapu', 'Enrique of Malacca'],
            correct_option='Enrique of Malacca'
        )
        QuizQuestion.objects.create(
            question="What is the longest river in the Philippines?",
            options=['Cagayan River', 'Agusan River', 'Pampanga River'],
            correct_option='Cagayan River'
        )
        QuizQuestion.objects.create(
            question="Which Philippine mountain is the highest peak in the country?",
            options=['Mount Mayon', 'Mount Apo', 'Mount Pulag'],
            correct_option='Mount Apo'
        )
        # Additional Questions - Part 7
        QuizQuestion.objects.create(
            question="Who is considered the father of modern computer science?",
            options=['Alan Turing', 'Bill Gates', 'Steve Jobs'],
            correct_option='Alan Turing'
        )
        QuizQuestion.objects.create(
            question="What does the acronym 'AI' stand for in the context of technology?",
            options=['Advanced Interface', 'Artificial Intelligence', 'Automated Invention'],
            correct_option='Artificial Intelligence'
        )
        QuizQuestion.objects.create(
            question="Which company developed the first commercially successful personal computer?",
            options=['IBM', 'Apple', 'Microsoft'],
            correct_option='Apple'
        )
        QuizQuestion.objects.create(
            question="What is the primary purpose of a 3D printer?",
            options=['Printing documents in 3D format', 'Creating three-dimensional objects layer by layer', 'Enhancing virtual reality experiences'],
            correct_option='Creating three-dimensional objects layer by layer'
        )
        QuizQuestion.objects.create(
            question="Which programming language is commonly used for web development?",
            options=['Java', 'Python', 'HTML/CSS'],
            correct_option='HTML/CSS'
        )
        QuizQuestion.objects.create(
            question="What is the main function of a firewall in computer security?",
            options=['Virus removal', 'Unauthorized access prevention', 'Data encryption'],
            correct_option='Unauthorized access prevention'
        )
        QuizQuestion.objects.create(
            question="Which tech company is associated with the slogan 'Think Different'?",
            options=['Microsoft', 'IBM', 'Apple'],
            correct_option='Apple'
        )
        QuizQuestion.objects.create(
            question="What is the purpose of a QR code in technology?",
            options=['Sending text messages', 'Storing and quickly retrieving information', 'Enhancing sound quality in audio files'],
            correct_option='Storing and quickly retrieving information'
        )
        QuizQuestion.objects.create(
            question="Which of the following is a widely used open-source operating system?",
            options=['Windows', 'macOS', 'Linux'],
            correct_option='Linux'
        )
        QuizQuestion.objects.create(
            question="What does the term 'IoT' stand for in the tech industry?",
            options=['Internet of Things', 'Input of Technology', 'Integrated Online Tools'],
            correct_option='Internet of Things'
        )
        QuizQuestion.objects.create(
            question="Who co-founded Microsoft alongside Bill Gates?",
            options=['Mark Zuckerberg', 'Steve Wozniak', 'Paul Allen'],
            correct_option='Paul Allen'
        )
        QuizQuestion.objects.create(
            question="Which technology is used for wireless communication between devices over short distances?",
            options=['Bluetooth', 'GPS', 'Wi-Fi'],
            correct_option='Bluetooth'
        )
        QuizQuestion.objects.create(
            question="What is the main purpose of a VPN (Virtual Private Network)?",
            options=['Enhancing internet speed', 'Securing and anonymizing online connections', 'Creating virtual reality environments'],
            correct_option='Securing and anonymizing online connections'
        )
        QuizQuestion.objects.create(
            question="What is the largest social media platform by active users?",
            options=['Instagram', 'Facebook', 'Twitter'],
            correct_option='Facebook'
        )
        QuizQuestion.objects.create(
            question="Which tech giant is known for its search engine?",
            options=['Apple', 'Google', 'Amazon'],
            correct_option='Google'
        )
        QuizQuestion.objects.create(
            question="What is the primary function of a drone in technology?",
            options=['Automated vacuum cleaning', 'Aerial photography and surveillance', 'Voice-controlled personal assistant'],
            correct_option='Aerial photography and surveillance'
        )
        QuizQuestion.objects.create(
            question="Which programming language is commonly used for data analysis and machine learning?",
            options=['Java', 'Python', 'C++'],
            correct_option='Python'
        )
        QuizQuestion.objects.create(
            question="What is the purpose of a CDN (Content Delivery Network) in internet infrastructure?",
            options=['Ensuring internet privacy', 'Accelerating content delivery and improving website performance', 'Blocking malicious websites'],
            correct_option='Accelerating content delivery and improving website performance'
        )
        QuizQuestion.objects.create(
            question="Which gaming console is developed by Sony?",
            options=['Xbox', 'Nintendo Switch', 'PlayStation'],
            correct_option='PlayStation'
        )
        QuizQuestion.objects.create(
            question="What is the concept of 'cloud computing' in technology?",
            options=['Storing data on physical servers', 'Accessing and using computing resources over the internet', 'Creating virtual reality simulations'],
            correct_option='Accessing and using computing resources over the internet'
        )
        QuizQuestion.objects.create(
            question="What is the primary function of a CPU (Central Processing Unit)?",
            options=['Graphics rendering', 'Data storage', 'Processing instructions'],
            correct_option='Processing instructions'
        )
        QuizQuestion.objects.create(
            question="Which component stores data permanently even when the power is turned off?",
            options=['RAM (Random Access Memory)', 'HDD (Hard Disk Drive)', 'CPU (Central Processing Unit)'],
            correct_option='HDD (Hard Disk Drive)'
        )
        QuizQuestion.objects.create(
            question="What does RAM stand for in computer hardware?",
            options=['Random Access Memory', 'Read-Only Memory', 'Redundant Array of Memory'],
            correct_option='Random Access Memory'
        )
        QuizQuestion.objects.create(
            question="Which type of connection is commonly used to connect peripherals such as printers and keyboards to a computer?",
            options=['USB (Universal Serial Bus)', 'HDMI (High-Definition Multimedia Interface)', 'VGA (Video Graphics Array)'],
            correct_option='USB (Universal Serial Bus)'
        )
        QuizQuestion.objects.create(
            question="What is the purpose of a GPU (Graphics Processing Unit) in a computer system?",
            options=['Data storage', 'Graphics rendering', 'Centralized processing'],
            correct_option='Graphics rendering'
        )
        QuizQuestion.objects.create(
            question="Which component is responsible for managing communication between different hardware devices in a computer?",
            options=['Motherboard', 'Power Supply Unit (PSU)', 'Network Interface Card (NIC)'],
            correct_option='Motherboard'
        )
        QuizQuestion.objects.create(
            question="What does BIOS stand for in computer hardware?",
            options=['Basic Input/Output System', 'Binary Input/Output Standard', 'Base Input/Output Software'],
            correct_option='Basic Input/Output System'
        )
        QuizQuestion.objects.create(
            question="Which storage technology is known for its fast data access but is volatile and loses data when power is interrupted?",
            options=['SSD (Solid State Drive)', 'HDD (Hard Disk Drive)', 'RAM (Random Access Memory)'],
            correct_option='RAM (Random Access Memory)'
        )
        QuizQuestion.objects.create(
            question="What is the purpose of a PSU (Power Supply Unit) in a computer?",
            options=['Process data', 'Provide power to components', 'Manage network connections'],
            correct_option='Provide power to components'
        )
        QuizQuestion.objects.create(
            question="Which of the following is not a type of computer port?",
            options=['USB', 'TCP', 'HDMI'],
            correct_option='TCP'
        )
        QuizQuestion.objects.create(
            question="What does RAID stand for in the context of data storage?",
            options=['Random Array of Independent Disks', 'Redundant Array of Inexpensive Disks', 'Rapid Access of Integrated Data'],
            correct_option='Redundant Array of Inexpensive Disks'
        )
        QuizQuestion.objects.create(
            question="Which component is responsible for converting digital signals from a computer into analog signals for transmission over telephone lines?",
            options=['Modem', 'Router', 'Switch'],
            correct_option='Modem'
        )
        QuizQuestion.objects.create(
            question="What is the purpose of a heat sink in a computer?",
            options=['Store data', 'Dissipate heat from the CPU', 'Amplify audio signals'],
            correct_option='Dissipate heat from the CPU'
        )
        QuizQuestion.objects.create(
            question="Which type of memory is non-volatile and retains data even when the power is turned off?",
            options=['RAM', 'ROM (Read-Only Memory)', 'Cache Memory'],
            correct_option='ROM (Read-Only Memory)'
        )
        QuizQuestion.objects.create(
            question="What is the role of a network interface card (NIC) in a computer?",
            options=['Process graphics', 'Connect to a network', 'Manage power supply'],
            correct_option='Connect to a network'
        )
        QuizQuestion.objects.create(
            question="Which technology allows wireless communication between devices within a short range?",
            options=['Bluetooth', 'NFC (Near Field Communication)', 'Wi-Fi'],
            correct_option='Bluetooth'
        )
        QuizQuestion.objects.create(
            question="What is the purpose of an optical drive in a computer?",
            options=['Display images', 'Read and write optical discs', 'Connect to the internet'],
            correct_option='Read and write optical discs'
        )
        QuizQuestion.objects.create(
            question="Which component is responsible for managing the flow of data between the CPU and other peripherals?",
            options=['Northbridge', 'Southbridge', 'Hard Drive Controller'],
            correct_option='Northbridge'
        )
        QuizQuestion.objects.create(
            question="What does HDMI stand for in the context of computer hardware?",
            options=['High-Definition Multimedia Interface', 'Hyperlink Data Management Interface', 'Hardware Direct Memory Interface'],
            correct_option='High-Definition Multimedia Interface'
        )
        QuizQuestion.objects.create(
            question="Which of the following is a common input device for a computer?",
            options=['Monitor', 'Keyboard', 'Speaker'],
            correct_option='Keyboard'
        )
        # Additional Questions - Part 9
        QuizQuestion.objects.create(
            question="What is a programming language?",
            options=['Set of cooking instructions', 'Formalized set of instructions that a computer can interpret', 'Ancient form of communication'],
            correct_option='Formalized set of instructions that a computer can interpret'
        )
        QuizQuestion.objects.create(
            question="Which programming language is known for its simplicity and readability?",
            options=['C++', 'Python', 'Java'],
            correct_option='Python'
        )
        QuizQuestion.objects.create(
            question="What does HTML stand for?",
            options=['HyperText Markup Language', 'High-level Text Language', 'HyperTransfer Markup Language'],
            correct_option='HyperText Markup Language'
        )
        QuizQuestion.objects.create(
            question="Which programming paradigm emphasizes immutability and functional purity?",
            options=['Object-oriented', 'Functional', 'Procedural'],
            correct_option='Functional'
        )
        QuizQuestion.objects.create(
            question="What is the purpose of a compiler in programming?",
            options=['To debug code', 'To translate source code into machine code', 'To design user interfaces'],
            correct_option='To translate source code into machine code'
        )
        QuizQuestion.objects.create(
            question="Which of the following is a dynamically typed language?",
            options=['Java', 'C#', 'JavaScript'],
            correct_option='JavaScript'
        )
        QuizQuestion.objects.create(
            question="What is the main advantage of version control systems like Git?",
            options=['Storing only the latest version of code', 'Collaborative development and version tracking', 'Running code on multiple machines simultaneously'],
            correct_option='Collaborative development and version tracking'
        )
        QuizQuestion.objects.create(
            question="Which company developed the C programming language?",
            options=['Microsoft', 'IBM', 'Bell Labs'],
            correct_option='Bell Labs'
        )
        QuizQuestion.objects.create(
            question="What is the purpose of SQL in programming?",
            options=['Styling web pages', 'Managing databases', 'Creating graphical user interfaces'],
            correct_option='Managing databases'
        )
        QuizQuestion.objects.create(
            question="Which programming language is commonly used for developing mobile applications?",
            options=['Swift', 'Ruby', 'PHP'],
            correct_option='Swift'
        )
        QuizQuestion.objects.create(
            question="What is the significance of the keyword 'this' in JavaScript?",
            options=['Refers to the previous function', 'Refers to the current object', 'Indicates the end of a statement'],
            correct_option='Refers to the current object'
        )
        QuizQuestion.objects.create(
            question="Which data structure follows the Last In, First Out (LIFO) principle?",
            options=['Queue', 'Stack', 'Linked List'],
            correct_option='Stack'
        )
        QuizQuestion.objects.create(
            question="What is the purpose of the 'else' statement in conditional structures?",
            options=['To repeat a block of code', 'To execute code only if a certain condition is false', 'To define a loop'],
            correct_option='To execute code only if a certain condition is false'
        )
        QuizQuestion.objects.create(
            question="In object-oriented programming, what is encapsulation?",
            options=['Hiding the implementation details and exposing only necessary functionalities', 'Combining multiple data types into one variable', 'Creating multiple instances of a class'],
            correct_option='Hiding the implementation details and exposing only necessary functionalities'
        )
        QuizQuestion.objects.create(
            question="Which programming language is commonly used for data analysis and statistics?",
            options=['Java', 'R', 'C#'],
            correct_option='R'
        )
        QuizQuestion.objects.create(
            question="What is the purpose of a constructor in object-oriented programming?",
            options=['To destroy objects', 'To initialize an object\'s properties', 'To create global variables'],
            correct_option='To initialize an object\'s properties'
        )
        QuizQuestion.objects.create(
            question="What does API stand for in the context of programming?",
            options=['Advanced Programming Interface', 'Application Programming Interface', 'Automated Programming Interface'],
            correct_option='Application Programming Interface'
        )
        QuizQuestion.objects.create(
            question="Which type of error occurs during compilation and prevents the program from running?",
            options=['Syntax error', 'Runtime error', 'Logic error'],
            correct_option='Syntax error'
        )
        QuizQuestion.objects.create(
            question="What is the purpose of the 'break' statement in loops?",
            options=['To exit the loop prematurely', 'To continue to the next iteration', 'To pause the loop temporarily'],
            correct_option='To exit the loop prematurely'
        )
        QuizQuestion.objects.create(
            question="Which programming language is commonly used for building web applications on the client side?",
            options=['Ruby', 'Python', 'JavaScript'],
            correct_option='JavaScript'
        )
        # Additional Questions - Part 10
        QuizQuestion.objects.create(
            question="What is drafting?",
            options=['Drawing plans', 'Writing documents', 'Cooking recipes'],
            correct_option='Drawing plans'
        )
        QuizQuestion.objects.create(
            question="Which tool is commonly used for freehand sketching?",
            options=['Compass', 'T-square', 'Pencil'],
            correct_option='Pencil'
        )
        QuizQuestion.objects.create(
            question="What does the term 'scale' refer to in drafting?",
            options=['Measurement tool', 'Drawing proportion', 'Punctuation mark'],
            correct_option='Drawing proportion'
        )
        QuizQuestion.objects.create(
            question="Which drafting tool helps draw straight horizontal lines?",
            options=['T-square', 'Protractor', 'French curve'],
            correct_option='T-square'
        )
        QuizQuestion.objects.create(
            question="What is the purpose of an eraser shield in drafting?",
            options=['Protecting erasers', 'Creating precise erasures', 'Shielding drafts from light'],
            correct_option='Creating precise erasures'
        )
        QuizQuestion.objects.create(
            question="Which type of line represents hidden features in a technical drawing?",
            options=['Dashed line', 'Solid line', 'Zigzag line'],
            correct_option='Dashed line'
        )
        QuizQuestion.objects.create(
            question="What does the term 'orthographic projection' mean in drafting?",
            options=['A type of pencil', 'A way to view 3D objects in 2D', 'A drafting board material'],
            correct_option='A way to view 3D objects in 2D'
        )
        QuizQuestion.objects.create(
            question="Which drafting tool is used for drawing arcs and circles?",
            options=['Compass', 'T-square', 'French curve'],
            correct_option='Compass'
        )
        QuizQuestion.objects.create(
            question="In drafting, what does the term 'CAD' stand for?",
            options=['Computer-Aided Design', 'Creative Artistic Drafting', 'Centralized Architectural Drawing'],
            correct_option='Computer-Aided Design'
        )
        QuizQuestion.objects.create(
            question="What is the purpose of a title block on a technical drawing?",
            options=['Adding decorative elements', 'Providing information about the drawing', 'Blocking unauthorized access'],
            correct_option='Providing information about the drawing'
        )
        QuizQuestion.objects.create(
            question="Which term refers to the angle between an inclined line and the horizontal?",
            options=['Slope', 'Gradient', 'Incline'],
            correct_option='Slope'
        )
        QuizQuestion.objects.create(
            question="What does the term 'drafting scale' indicate?",
            options=['A ruler with only odd numbers', 'A scale used for rough drafts', 'A scale for precise measurements in drafting'],
            correct_option='A scale for precise measurements in drafting'
        )
        QuizQuestion.objects.create(
            question="Which drafting term is associated with the process of making a copy of a drawing?",
            options=['Duplicating', 'Replicating', 'Cloning'],
            correct_option='Duplicating'
        )
        QuizQuestion.objects.create(
            question="What is the purpose of a compass in drafting?",
            options=['Drawing straight lines', 'Measuring distances', 'Drawing circles and arcs'],
            correct_option='Drawing circles and arcs'
        )
        QuizQuestion.objects.create(
            question="Which type of projection shows an object as it appears to the eye?",
            options=['Isometric projection', 'Perspective projection', 'Orthographic projection'],
            correct_option='Perspective projection'
        )
        QuizQuestion.objects.create(
            question="What is the role of a triangle in drafting?",
            options=['Drawing circles', 'Creating angular lines', 'Measuring lengths'],
            correct_option='Creating angular lines'
        )
        QuizQuestion.objects.create(
            question="Which term refers to the space between lines on a drawing?",
            options=['Interval', 'Spacing', 'Gap'],
            correct_option='Spacing'
        )
        QuizQuestion.objects.create(
            question="What does the acronym 'ISO' stand for in the context of drafting standards?",
            options=['International Standards Organization', 'Industrial Sketching Organization', 'Intra-Sectoral Organization'],
            correct_option='International Standards Organization'
        )
        QuizQuestion.objects.create(
            question="In drafting, what is the purpose of hatching or cross-hatching?",
            options=['Adding shading for depth', 'Enhancing color', 'Securing the drawing paper'],
            correct_option='Adding shading for depth'
        )
        QuizQuestion.objects.create(
            question="Which drafting tool is used for drawing smooth curves and irregular shapes?",
            options=['T-square', 'Compass', 'French curve'],
            correct_option='French curve'
        )
