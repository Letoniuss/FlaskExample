from flask import Flask, make_response, Response
from MyWaves import MyWaves
application = Flask(__name__)

@application.route('/')
def hello_world():
    OhHi = "Oh, so you were looking to run a report? Well, I can't do that but I can ask how you are doing today! How are you?"
    MkWv = "Also, let's make waves!"
    wave = MyWaves(25)
    wave.SquareWave()
    wave.ApproxSqWave()
    FigOut = wave.PlotWaves()
    DnWv = "Now those are some waves!"
    NewLn = "\n"
    output = f"{OhHi}{NewLn}{NewLn}{MkWv}{NewLn}{NewLn}{DnWv}{NewLn}"
    print(output)
    #response = make_response(output.encode())
    #response.mimetype = "text/plain"
    return Response(FigOut.getvalue(), mimetype='image/png')

