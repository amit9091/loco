import discord

def  init():
    global bot_token
    global self_bot_token
    global message
    global embed
    global output_channel
    global input_channels
    global command_channel

    global game_in_session
    global counter_public_1
    global counter_public_2
    global counter_public_3
    global counter_private_1
    global counter_private_2
    global counter_private_3
    global counter1
    global counter2
    global counter3
    global weight
    global weight_time
    global seconds_elapsed

bot_token = 'NTg0MjQ2NDExOTkwNjYzMjA1.XULUjw.HDMLswJ5l2ojJhzZLs2wnqNHQOU'
self_bot_token = 'NTk3OTY2MTI1NzM2NjU2OTA2.XTnbng.O4W_i-O7rxKp80SFwv4E7BlpbF8'

message = None
embed = None
embed_best = None

#trivia-answers
output_channel = discord.Object(id= '587999534022393866'
			       


input_hq_private  = [
    "604231562740891659",
    "593990638916075520",
    "590583414541910018",
	    "595640668924280848",
	    "588070986554015764",
	    "590109407950667776",
	    "590074693097095168",
	    "588413537907376180",
	    "590182835948879872",
	    "570257859850272788",
	    "590471026899550208",
	    "589120764347678750",
	    "585682137202819101",
	    "590470896649502750",
	    "590182635653824542",
	    "589120764347678750",
	    "589516793350062100",
    "583796470394781696",
    "604231562740891659", # answers1
    "559442345674670082", #answers2
    '577486564402397194' #trivia-answers
]
input_hq_public = ['604231562740891659']
command_channel = '604231562740891659' #trivia-answers
admin_chat = '604231562740891659' # answers2

game_in_session = False
counter_public_1 = 0
counter_public_2 = 0
counter_public_3 = 0
counter_private_1 = 0
counter_private_2 = 0
counter_private_3 = 0
counter1 = 0
counter2 = 0
counter3 = 0
weight = 5
weight_time = 1
wronggone1 = 0
wronggone2 = 0
wronggone3 = 0

seconds_elapsed = 0

