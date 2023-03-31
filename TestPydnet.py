import torch
import torch.nn as nn

class ConvLeaky(nn.Module):

    def __init__(self, i, ic, oc, ks, ss, ps):
        super(ConvLeaky, self).__init__()

        sequence = nn.Sequential()
        sequence.add_module('conv{0}'.format(i), nn.Conv2d(ic, oc, ks, ss, ps))
        sequence.add_module('relu{0}'.format(i), nn.LeakyReLU(0.2, inplace=True))

        self.convLeaky = sequence

    def forward(self, input):
        output = self.convLeaky(input)

        return output

class DeconvLeaky(nn.Module):

    def __init__(self, i, ic, oc, ks, ss, ps):
        super(DeconvLeaky, self).__init__()

        sequence = nn.Sequential()
        sequence.add_module('conv{0}'.format(i), nn.ConvTranspose2d(ic, oc, ks, ss, ps))
        sequence.add_module('relu{0}'.format(i), nn.LeakyReLU(0.2, inplace=True))

        self.deconvLeaky = sequence

    def forward(self, input):
        output  = self.deconvLeaky(input)

        return output

class Disperity(nn.Module):

    def __init__(self):
        self.relu = 

    def forward(self, input):
        left = torch.index_select(3, 0)
        right = torch.index_select(3, 1)
        disparity = [left, right]
        return disparity

class CnnPyramid(nn.Module):

    def __init__(self, ic):
        super(CnnPyramid, self).__init__()

        ks = [3, 3, 3, 3, 3, 3, 3, 3]
        ss = [2, 1, 2, 1, 2, 1, 2, 1]
        ps = [0, 0, 0, 0, 0, 0, 0, 0]
        oc = [16, 16, 32, 32, 64, 64, 96, 96]

        # output w = (w - ks + 1) / stride
        # output h = (h - ks + 1) / stride
        # Input a 256x256x3 image, run through a 3x3x3 filter by stride 2, output 127x127x16 image
        self.convLeaky_1 = ConvLeaky(1, ic, oc[0], ks[0], ss[0], ps[0])
        # Input 127x127x16 image, run through a 3x3x16 filter by stride 1, output 125x125x16 image
        self.convLeaky_2 = ConvLeaky(2, oc[0], oc[1], ks[1], ss[1], ps[1])
        # Input 125x125x16 image, run through a 3x3x16 filter by stride 2, output 62x62x32 image
        self.convLeaky_3 = ConvLeaky(3, oc[1], oc[2], ks[2], ss[2], ps[2])
        # Input 62x62x32 image, run through a 3x3x32 filter by stride 1, output 60x60x32 image
        self.convLeaky_4 = ConvLeaky(4, oc[2], oc[3], ks[3], ss[3], ps[3])
        # Input 60x60x32 image, run through a 3x3x32 filter by stride 2, output 29x29x64 image
        self.convLeaky_5 = ConvLeaky(5, oc[3], oc[4], ks[4], ss[4], ps[4])
        # Input 29x29x64 image, run through a 3x3x64 filter by stride 1, output 27x27x64 image
        self.convLeaky_6 = ConvLeaky(6, oc[4], oc[5], ks[5], ss[5], ps[5])
        # Input 27x27x64 image, run through a 3x3x64 filter by stride 2, output 13x13x96 image
        self.convLeaky_7 = ConvLeaky(7, oc[5], oc[6], ks[6], ss[6], ps[6])
        # Input 13x13x96 image, run through a 3x3x96 filter by stride 1, output 11x11x96 image
        self.convLeaky_8 = ConvLeaky(8, oc[6], oc[7], ks[7], ss[7], ps[7])

    def forward(self, input):
        output_1 = self.convLeaky_1(input)
        output_2 = self.convLeaky_2(output_1)
        output_3 = self.convLeaky_3(output_2)
        output_4 = self.convLeaky_4(output_3)
        output_5 = self.convLeaky_5(output_4)
        output_6 = self.convLeaky_6(output_5)
        output_7 = self.convLeaky_7(output_6)
        output_8 = self.convLeaky_8(output_7)

        return output_8

class Estimator:

    def __init__(self):
        self.convLeaky_1 = ConvLeaky(1, 96, 96, 3, 1, 0)
        self.convLeaky_2 = ConvLeaky(2, 96, 64, 3, 1, 0)
        self.convLeaky_3 = ConvLeaky(3, 64, 32, 3, 1, 0)
        self.convLeaky_4 = ConvLeaky(4, 32, 8, 3, 1, 0)

    def run_estimator(input):
        output_1 = self.convLeaky_1(input)
        output_2 = self.convLeaky_2(output_1)
        output_3 = self.convLeaky_3(output_2)
        output_4 = self.convLeaky_4(output_3)

        return output_4

    

