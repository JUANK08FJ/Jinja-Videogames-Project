from jinja2 import *
import json
import os


# JSON LOADED IN A VARIABLE
json_base = open("dis_gms.json", "r")
json_data = json.load(json_base)


# VARIABLES FOR THE THREE TEMPLATES
tindex = Template(open("templates/index.html", "r").read())
tcss = Template(open("templates/main.css", "r").read())
tdistributor = Template(open("templates/distributor.html", "r").read())
tgame = Template(open("templates/game.html", "r").read())


#  DIRECTORIES
if not os.path.exists("./pages"):
    os.makedirs("./pages/videogames")
    os.makedirs("./pages/distributors")
else:
    if not os.path.exists("./pages/videogames"):
        os.makedirs("./pages/videogames")
    
    if not os.path.exists("./pages/distributors"):
        os.makedirs("./pages/distributors")

# RENDER
page_render = tindex.render(jdistributors=json_data["distributors"], jgames=json_data["games"],
                            jdeveloper=json_data["developer"])
css_render = tcss.render(jdistributors=json_data["distributors"])


# REWRITE
findex = open("pages/index.html", "w")
findex.write(page_render)
findex.close()

fcss = open("pages/main.css", "w")
fcss.write(css_render)
fcss.close()


# RENDER AND WRITE
for distributor in json_data["distributors"]:
    distributor_render = tdistributor.render(distributor=distributor, jdistributors=json_data["distributors"],
                                             jgames=json_data["games"],
                                             jdeveloper=json_data["developer"])
    fdistributor = open("pages/distributors/" + distributor["urlName"], "w")
    fdistributor.write(distributor_render)
    fdistributor.close()

for game in json_data["games"]:
    game_render = tgame.render(game=game, jdistributors=json_data["distributors"], jgames=json_data["games"],
                               jdeveloper=json_data["developer"], jgenres=game["genres"], jgameStudio=game["gameStudio"])
    fgame = open("pages/videogames/" + game["urlName"], "w")
    fgame.write(game_render)
    fgame.close()
