import json
fertilizers = {
    'rice':
    {
        'tungro':
        {
            "about": "It is caused by a virus that affects every growing stage and severely affects the vegetative stage.this virus transmitted by green leafhopper which is the most efficient vector for spread.Plants show stunting and reduced tillering and yield.\n the following will help you to identify the damage.\n1.Yellow or Orange spots froms the leaf tip to the blade or lower leaf portion.\n 2.Colored patch or striped leaves and damage between leaf veins.\n3.Stunting of plants and reducing the number of tillers.",
            "chemical_control":
            {
                "chemical_name": "Mancozeb 75% WP+Urea 500g/Acre",
                "brands": [r'brands/rice/tungro/brand1.png', r'brands/rice/tungro/brand2.png'],
                "how_to_apply":"Spray uniformly on the plants at disease initiation to manage the yellowing leaf, later apply specified fungicide as mentioned in the list.Repeat the applications at 7-12 days interval depending on climatic conditions and disease severity.Dilute the recommended dosage of chemicals with 200 liters of water per acre. Take the required amount of chemicals and dilute separately with few liters of water in a bucket and then pour both solutions into a spray tank and add remaining amount of water with continuous 		stirring. Avoid mixing alkaline water. The spray volume of solution may vary depending on crop growth stage and spacing To make 2% Urea solution you have to mix 2kg of Urea in 100 liters of water. (20g in 1 liter of water) you should be cautious with application of high urea concentrations with possible leaf injury/burning. Instead of urea foliar fertilizer like Potassium nitrate can be sprayed at 1% (100g in 200 liters of water) which impart resistance also because of high potassium content."
            },
            "biological_control":
            {
                "name_of_bioagent":"neem cake 50 Kg/ Acre",
                "brands":[r'brands/rice/tungro/brand3.png'],
                "how_to_apply":"Apply in the nursery at the time of last ploughing of soil for 3-4 weeks before sowing. Plough the soil deeply and mix the recommended rate of Neem Cakes thoroughly before the irrigation cycle. When you do it this way, it gives you better results than if you only apply it to ground's surface. Since Neemcake acts as a slow-release, multiple irrigations might be required before results can be observed."
            },
            "cultural_control": 
            {
                "process":"light trap",
                "how_to_apply":"Install 1 or 2 light traps at 5 to 8 feet above the ground withing the field from 6pm to the early morning/Use fluorescent or mercury buld 	in the trap.PLace a tray with soap water or insecticide solution(cyber-10,ACUTE-100) below the light",
                "others":"Remove all the diseased plant parts and bury into the soil.\nSeedings have to be kept insect free up to 40-50  days after transplanting.\nAdd paddy straw into the soil immediately after harvest.\nSelect leafhopper or virus-resistant varieties.\nleave the field  uncultivated 30 days  after harvest.\nIn severe areas follow rotation with pulses or oilseeds.\nDestroy stubbles right after harvest to eradicate other tungro hosts."
            }
        },
        'blast':
        {
            "about": "it is a fungal disease.it is more severe in areas where the rainfall and humidity is high.losses due to this disease may be go up to 90% of total crop.",
            "chemical_control":
            {
                "chemical_name": "Captan , Carbendazim , Thiram and Tricyclazole.",
                "brands":[r'brands/rice/blast/brand1.png', r'brands/rice/blast/blast_bio.png'],
                "how_to_apply":"Seed treatment at 2.0 g/kg seed with Captan or Carbendazim or Thiram or Tricyclazole.\nSpraying of Tricyclazole at 1g/lit of water or Edifenphos at 1 ml/lit of water or Carbendazim at 1.0 gm/lit.\n3 to 4 sprays each at nursery, tillering stage and panicle emergence stage may be required for complete control.\n	Nursery stage: Light infection - Spray Carbendazim or Edifenphos @ 1.0 gm/lit.\nPre-Tillering to Mid-Tillering: Light at 2 to 5 % disease severities - Apply Edifenphos or Carbendazim @ 1.0 gm/lit. Delay top dressing of N fertilizers when infection is seen.\nPanicle initiation to booting: At 2 to 5% leaf area damage- spray Edifenphos or Carbendazim or Tricyclazole @ 1.0 gm/lit.\nFlowering and after: At 5 % leaf area damage or 1 to 2 % neck infection spray Edifenphos or Carbendazim or Tricyclazole @ 1 g /lit of water."
            },
            "biological_control": 
            {
                "name_of_bioagent":"Mycorrhiza 1000 IP Powder",
                "brands":[r'brands/rice/blast/myco.png'],
                "how_to_apply":"None",
            },
            "cultural_control": 
            {
                "process":'None',
                "how_to_apply":"None",
                "others":"Planting resistant varieties against the rice blast is the most practical and economical way of controlling rice blast.\n Use of Tolerant varieties (CO 47, CO 50, ADT 36,ADT 37,ASD 16,ASD 20,ADT 39,ASD 19,TPS 3,White ponni,ADT 44,BPT 5204,CORH ,Palghuna, Swarnamukhi, Swathi,Prabhat, IR - 64, , IR - 36, Jaya)\nAvoid excess N - fertilizer application.\nApply nitrogen in three split doses.\nRemove weed hosts from bunds."
            }
        },
        'bacterial-blight':
        {
            "about":"If the incidence percentage is 2-5% of (2-3infected leaves per square meter area)plants are affected, then go for controlmeasures.Apply any one of the following chemical;if the disease is not controlled, pleasefollow up with other chemical from the listbelow based on the specific duration of thepreviously applied chemical.",
            "chemical_control":
            {
                "chemical_name":"Streptomycin Sulphate 9% +Tetracycline Hydrochloride 1% SP",
                "brands":[],
                "how_to_apply":"Preparation of Spray Mixture:- Dissolve required quantity of Streptocycline directly in 10 liter of water and make up the desired volume by remaining quantity of water"
            },
            "biological_control":
            {
                "name of bioagent":"Neem Seed Kernel Extract (NSKE),Pseudomonas fluorescens (L)",
                "brands":"None",
                "how_to_apply":"n the early morning or evening for better results. If the disease is not controlled,please follow up with alternative bioagents"
            },
            "cultural_control":
            {
                "process":"Drain the field (except at the flowering stage of the crop).Remove commonly affected plantsand weeds near paddy fields andharvest at the ground level.Do not allow irrigated water to flowfrom an infected to healthy field.Avoid excess usage of nitrogenousfertilizers. Apply Nitrogen in threesplit doses, 50% basal, 25% intillering phase and 25% in the panicleinitiation stage).",
                "how_to_apply":"None",
                "others":"None",
            }
        },
        'brown-spot':
        {
            "about":"f you see 2-3 spots on the leaf and 2-3infected plants per meter square than go",
            "chemical_cntrol":
            {
                "chemical_name":"Carbendazim 12% + Mancozeb 63%WP",
                "brands":[],
                "how_to_apply":"Smart Carbendazim 500 SC Fungicide is a liquid suspension to be mixed with water for application as a spray. Add the required quantity of Smart Carbendazim 500 SC Fungicide to a partly filled spray tank and agitate. Complete filling while agitating."
            },
            "biological_control":
            {
                "name_of_the_bioagent":"Pseudomonas fluorescens (P),Pseudomonas fluorescens (P),Farm Yard Manure (FYM)",
                "brands":"None",
                "how_to_apply":"Apply any one of the following bioagents in the early morning or evening for better results. If the disease is not controlled,please follow up with alternative bioagents."
            },
            "cultural_control":
            {
                "process":"Monitor soil nutrients regularly and apply required fertilizers.Soak the seeds in hot water at53-540C for 10-12 minutes.",
                "how_to_apply":"None",
                "others":"None",
            }
        }
    },

    'potato':
    {
        'early-blight':
        {
            "about": "it is fungal disease.a group ofspecies of fungal genus Alteraria causes this disease.The wind and rain splashing spread the spores.High temperatures(20-25 degree C) and dew at night are favourable conditions for the development.These leaf spots may cause significant yield loss of up to 20% in Kharif.The disease symptoms occur during the tuber bulking stage and development leading to the harvest.Foliage at any stage of the growth and causes leaf spots and blight.the following symptoms will help you to identify the disease.\n Lower and older leaves with small(1-2mm),circular to oval,brown concentric rings/spots./n Several spots come together and spread all over the leaf.\n Mature wounds on foliage look dry and papery and often have concentric ring,looking loke a bulls-eye.\n The tubers show brown,circular to irregular,and depressed lesions./n Lesions underneath flesh turn dry,brown,and corky.Affected tubers later become shriveled.",
            "chemical_control":
            {
                "chemical_name": "Mancozeb 75% WP 600 g/Acre",
                "brands": [r'brands/rice/tungro/chemical.png', r'brands/rice/tungro/early.png'],
                "how_to_apply":"Spray uniformly on the plant.Dilute the recommended dosage of chemical with 200 liters of water per acre. Take the required amount of chemical and dilute 			separately with a small amount of water to create slurry without lumps in a bucket and pour it into a spray tank and add the remaining amount of water with continuous stirring. Avoid mixing alkaline water. Do constant agitation in the spray tank to avoid 		blockages in nozzles and filters. The spray volume of solution may vary depending on crop growth stage and spacing. Repeat the spray 2-3 times at 10-15 days of intervals depending upon severity.Azoxystrobin 11% + Tebuconazole 18.3% SC (300ml/Acre)Spray uniformly on the plant.Dilute the recommended dosage of chemical with 200 liters of water per acre. Shake the chemical container properly before use. Take the required amount of chemical and dilute separately with few liters of water in a bucket and pour it into a spray tank and add remaining amount of water with continuous stirring. Avoid mixing alkaline water. Do constant agitation in the spray tank. The spray volume of solution may vary depending on crop growth stage and spacing."
            },
            "biological_control": 
            {
                "name_of_bioagent":"Bacillus subtilis (L)(1 Kg/Acre)",
                "brands":r'brands/potato/early blight/bio_agent.png',
                "how_to_apply":"Spray uniformly on the plant. Dilute the recommended dosage of bioagent with 200 liters of water per acre. Take the required 			amount of bioagent and dilute separately with a small amount of water to make slurry without lumps in a bucket and pour it into a 		spray tank through filter and add remaining amount of water with continuous stirring. Always filter while adding the content into 		spray tank. Avoid mixing alkaline water or chemical for mixing. Do constant agitation in the spray tank to avoid blockages in 			nozzles and filters. Repeat the spray 2-3 times at 7-10 days of intervals depending upon severity. Prepare a fresh batch for each spray. The spray volume of solution may vary depending on crop growth stage and spacing.Trichoderma harzianum (P)(1 Kg/Acre)"
            },
            "cultural_control": 
            {
                "process":"None",
                "how_to_apply":"None",
                "others":">Remove all the diseased plant parts and destroy.\n Maintain the proper plant spacing for good aeration.\n Avoid prolonged moisture in the field.\n Grow disease-resistant /tolerant varieties.\n Rotate crops with non_host,such as legume crops for 2 years.\n To reduce soil -borne pathogens,do deep ploughing hot summer day."
            }
        },
        'late-blight':
        {
            "about":"It is a fungal disease,widespread in hilly areas,but it is less severe in plains.Susceptible cultivars are killed in 8 to 10 days of the disease appearance,whereas it takes 10 to 15 days in resistant varieties.The pathogens causes purplish-brown woundson the aurface of tubers and then unfit for consumption and marketing.Late blight affects all plant parts,especially leaves,stems abd tubers.the disease primarly starts at basal leaves and spreads upwards.the following symptoms will help you to identify the disease.\n Water-soaked spots(2-10mm) on leaves margin and tips,size increases ,turns purple_brown,and finally turns dead black.\n Whitish cottony growth develops around the dead area in a ring pattern under the leaves.\n On the stem,light brown lesions develop,elongating and encircling the stema dn petioles and instantly killing the plant or leaves.",
            "chemical_control":
            {
                "chemical_name": "Iprovalicarb 5.5%+Propineb 61.25% WP 800g/Acre",
                "brands": [r'brands/potato/late blight/chemical brand.png', r'brands/potato/late blight/ip.png'],
                "how_to_apply":"Spray uniformly on the plant.Dilute the recommended dosage of chemical with 200 liters of water per acre. Take the required amount of chemical and dilute with a small amount of water to create slurry without lumps in a bucket and then pour into a spray tank and add remaining amount of water with continuous stirring. Avoid mixing alkaline water. Do constant agitation in the spray tank to avoid blockages in nozzles and filters. The spray volume of solution may vary depending on crop growth stage and spacing."
            },
            "biological_control":
            {
                "name_of_bioagent":"Bacillus subtilis(L) 1 Kg/ Acre",
                "brands":r'brands/potato/late blight/bio_agent.png',
                "how_to_apply":"Spray uniformly on the plant.Dilute the recommended dosage of bioagent with 200 liters of water per acre. Take the required amount of bioagent and dilute separately with a small amount of water to make slurry without lumps in a bucket and pour it into a spray tank through filter and add remaining amount of water with continuous stirring. Always filter while adding the content into spray tank. Avoid mixing alkaline water or chemical for mixing. Do constant agitation in the spray tank to avoid blockages in nozzles and filters. Repeat the spray 2-3 times at 7-10 days  of intervals depending upon severity. Prepare a fresh batch for each spray. The spray volume of solution may vary depending on crop growth stage and spacing."
            },
            "cultural_control":
            {
                "process":"None",
                "how_to_apply":"None",
                "others":"Grow disease-resistant/tolerant varieties.\n Maintain the proper plant spacing for good aeration.\n avoid dry spell and irrigate field at regular intervals.\n Avoid excess usage of nitrogenous fertilizers.\n Avoid doing intercultural activities during the wet reson.\n Minimize irrigation after the blight has set in and by cutting haulms."
            }
        }
    },

    'capsicum':
    {
        'bacterial-tcanker':
        {
            "about":"It is a bacterial disease,the bacterium enters the plant via wounds and maybe a seed-borne infection.Insects,tools,and human contacct spread the disease.High relative humidity and daytime temperatures between 25 to 30 degree Centigrade favours the disease development.The follwoing symptoms will help you to identify the disease.",
            "chemical_control":
            {
                 "chemical_name":"Famoxadone 16.6% + Cymoxanil 22.1% SC 200ml/ Acre",
                 "brands":[r'brands/capsicum/ch.png',r'brands/capsicum/chaa.png'],
                 "how_to_apply":"Spray uniformly on the plant.Dilute the recommended dose of chemical with 200 liters of water per acre. Shake the chemical container properly before use. Take the required amount of chemical and dilute with few liters of water in a bucket, pour into a spray tank, and add the remaining amount of water with continuous stirring. Avoid mixing alkaline water. Do constant agitation in the spray tank. The spray volume of a solution may vary depending on crop growth stage and spacing.Do not spray if you are planning to harvest within 3 days."
            },
            "biological_control":
            {
                "name_of_bioagent":"Bacillus sybtilis (P) 1Kg/Acre",
                "brands":[r'brands/capsicum/bio.png',r'brands/capsicum/bio2.png'],
                "how_to_apply":"Spray uniformly on the plant. Dilute the recommended dosage of bioagent with 200 liters of water per acre. Take the required amount of bioagent and dilute with a small amount of water to make slurry without lumps in a bucket and then pour into a spray tank through a filter and add the remaining amount of water with continuous stirring. Always filter while adding the content into the spray tank. Avoid mixing alkaline water or chemical. Do constant agitation in the spray tank to avoid blockages in nozzles and filters."
            },
            "cultural_control":
            {
                "process":"organic fertilizers",
                "how_to_apply":"None",
                "others":"Uproot severely infested plants and dispose of them properly. Maintain the proper plant spacing for Maintain the proper plant spacing for good aeration.Avoid prolonged moisture in the field. Avoid overhead watering Don't plant Brinjal, tomatoes, and tobacco during the rotation period.Do deep ploughing during summer."
            }
        }        
    },

    'tomato':
    {
        "bacterial-spot":
        {
            "about":"It is a bactorial disease which survives in infected crop remains,seeds,in other hosts,and weeds.Moist and warm (24 to 30oC) weather and high humidity are favourable for the disease spread and development.The disease causes leaf and fruit spots leading to defoilation.",
            "chemical_control":
            {
                "chemical_name":"Streptomycin Sulphate 9% +Tetracycline Hydrochloride 1% SP (20 g/Acre)",
                "brands":[r'brands/tomato/bacterial spot/chem.png',r'brands/tomato/bacterial spot/anu.png'],
                "how_to_apply":"Spray uniformly on the plant.Dilute the recommended dosage of chemical with 200 liters of water per acre. Take the required amount of chemical and dilute separately with few liters of water in a bucket and pour it into a spray tank and add remaining amount of water with continuous stirring. Avoid mixing alkaline water. Do constant agitation in the spray tank. The spray volume of solution may vary depending on crop growth stage and spacing."
            },
            "biological_control":
            {
                "name_of_bioagent":"Bacillus subtilis (L) 1 Kg/ Acre",
                "brands":r'brands/tomato/bacterial spot/bio.png',
                "how_to_apply":"Spray uniformly on the plant. Dilute the recommended dosage of bioagent with 200 liters of water per acre. Take the required amount of bioagent and dilute separately with a small amount of water to make slurry without lumps in a bucket and pour it into a spray tank through 	filter and add remaining amount of water with continuous stirring. Always filter while adding the content into spray tank. Avoid mixing alkaline water or chemical for mixing. Do constant agitation in the spray tank to avoid blockages in nozzles and filters. Repeat the spray 	2-3 times at 7-10 days of intervals depending upon severity. Prepare a fresh batch for each spray. The spray volume of solution may vary depending on crop growth stage and spacing."
            },
            "cultural_control":
            {
                "process":"None",
                "how_to_apply":"None",
                "others":"Maintain a weed free field, bunds,irrigation channel and surroundings.\nDo not allow irsrigated water to flow from an infected to healthy field.\nAvoid water stagnation and maintain proper drainage.Remove all the diseased plant parts and bury them into the soil.\nSterilize the tools and equipments with alcohol that are used for pruning."
            }
        },
        "leaf-mold":
        {
            "about":"It is fungal disease.This fungus can infect all above ground parts of the plant.Cool temperatures(15-23o C),high humudity favours disease growth.Close spacing and poor ventilation can lead to severe leaf mold probem.\n The following symptoms will help you to identify the disease.\n 1.The v-shaped lesion covered with grey fungus appears on leaves.\n 2.Elliptical,water_soaked lesions appear on the stem.\n 3.Lesions surface covered by grey mold causing girdles and kill the plant.\n 4.Stem lesions often show concentric banding.\n 5.The calyx end of the fruit show lesion with grey-brown sporulating that later develops into a watery rot.\n 6.Small white to pale yellow or green rings on green or red fruit.",
            "chemical_control":
            {
                "chemical_name":"Azoxystrobin 8.3% + Mancozeb 66.7% WG 600g/Acre",
                "brands":[r'brands/tomato/leaf mold/bran2.png',r'brands/tomato/leaf mold/chemical brand.png'],
                "how_to_apply":"Spray uniformly on the plant.\nDilute the recommended dosage of chemical with 200 liters of water per acre.\n Take the required amount of chemical and dilute separately with few liters of water in a bucket and pour it into a spray tank and add remaining amount of water with continuous stirring. \nAvoid mixing alkaline water. \n Do constant agitation in the spray tank to avoid blockages in nozzles and filters.\n The spray volume of solution may vary depending on crop growth stage and spacing.\nDo not tank-mix with EC formulation."
            },
            "biological_control":"Currently,no effective biological control measures available for this disease",
            "cultural_control":
            {
                "process":"1.Remove infected plants and destroy them.\n 2.Avoid excess nitrogen application.\n 3.Maintain a weed free field,bunds,irriagtion channel and surroundings.\n 4.Maintain the proper plant spacing for good aeration.\n 5.Avoid water stagnation and maintain proper drainage.\n 6.To reduce soil-borne pathogens,do deep ploughing during hit summer day. ",
                "how_to_apply":"None",
                "others":"None",
            }
        },
        "mosaic-virus":
        {
            "about":"Tomato mosaic virus symptoms can be found at any stage of growth and all parts of the plant may be infected. They are often seen as a general mottling or mosaic appearance on foliage.",
            "chemical_control":
            {
                "chemical_name":"Currently, no effective chemical control measures are available for this disease.",
                "brands":[],
                "how_to_apply":"None",
            },
            "biological_control":"Currently, no effective biological control measures available for this disease.",
    
            "cultural_control":
            {
                "process":"Uproot severely infested plants an dispose properly.Plant disease free material.Grow resistant or tolerant varieties.",
                "how_to_apply":"None",
                "others":"None",
            }
        },
    
        "septoria-spot":
        {
            "about":"Apply any one of the following chemicals;if the disease is not controlled, please follow up with other chemicals from the listbelow based on the specific duration of the previously applied chemical.",
            "chemical_control":
            {
                "chemical_name":"Copper Hydroxide 77% WP",
                "brands":[],
                "how_to_apply":"None",
            },
            "biological_control":
            {
                "name of the  bioagent":"None",
                "others":"None",
                "how_to_apply":"Apply following bioagent in the early morning or evening for better results. If thedisease is not controlled, please schedulefollow-up sprays with the same bioagentsif required with specific intervals.Bacillus subtilis (L)",
  
            },
            "cultural_control":
            {
                "process":"Maintain a weed free field, bunds,irrigation channel and surroundings.Do not allow irrigated water to flowfrom an infected to healthy field.Avoid water stagnation and maintain proper drainage.",
                "how_to_apply":"None",
                "others":"None",
            }
        },
        "spider-kite":
        {
            "about":"Apply any one of the following chemicals;if the pest is not controlled, please followup with other chemicals from the list belowbased on the specific duration of thepreviously applied chemical.",
            "chemical_control":
            {
                "chemical_name":"Fenazaquin 10% EC",
                "brands":[],
                "how_to_apply":"Inject specified amount of FENPYROXIMATE 40WG miticide/ insecticide per acre for: (1) a continuous 20 to 40-minute period at the end of a regular irrigation set."
            },
            "biological_control":
            {
                "name of the bioagent":"None",
                "brands":"None",
                "how_to_apply":"Apply following bioagent in the early morning or evening for better results. Ifthe pest is not controlled, please schedule",
                
            },
            "cultural_control":
            {
                "process":"None",
                "how_to_apply":"Remove all the crop debris and always maintains the field weed-free.Provide jet water spray on plants,make plants wet so that mites will not survive in wet conditions.",
                "others":"None",
                
            }
            
        }
}
    }

with open('fertilizers_final.json', 'w') as f:
    json.dump(fertilizers, f)
