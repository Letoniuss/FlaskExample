import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io

class MyWaves:
    def __init__(self, NumHarmonics = 5):
        self.NumPts =NumPts = 2000000
        self.Periods = Periods = 5
        self.w = w = 1.0e3  # hertz

        self.tLength = tLength = Periods/w  # seconds
        self.t = np.linspace(0, tLength, NumPts)
        self.NumHarmonics = NumHarmonics
        self.PeriodsToShow = Periods
        pass

    def SquareWave(self):
        self.PSq = PSq = np.zeros_like(self.t)
        PSq[::] = np.sin(2*np.pi*self.w*self.t)
        for jj, p in enumerate(PSq):
            if p >= 0.0:
                PSq[jj] = 1.0
            else:
                PSq[jj]= -1.0
        pass

    def ApproxSqWave(self):
        self.PASq = PASq = np.zeros_like(self.t)
        for ii in range(1,2*self.NumHarmonics+1,2):
            PASq += 4/np.pi*np.sin(2*np.pi*self.w*ii*self.t)/ii
        pass


    def PlotWaves(self):
        fig = Figure()
        axis = fig.add_subplot(1, 1, 1)
        axis.plot(self.t, self.PSq)
        axis.plot(self.t, self.PASq)
        axis.set_xlim((0, self.PeriodsToShow/self.w))
        axis.grid()
        fig.tight_layout()
        output = io.BytesIO()
        FigureCanvas(fig).print_png(output)
        return output
