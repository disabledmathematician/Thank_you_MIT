import pandas as pd
import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt
# Charles Thomas Wallace Truscott Watters
# 127 Broken Head Rd, Suffolk Park / Byron Bay NSW 2481
def main():
    sines = np.array([(np.sin(np.pi / 180 * x)) for x in range(-360, 361)])
    cosines = np.array([(np.cos(np.pi / 180 * x)) for x in range(-360, 361)])
    tangents = np.array([(np.sin(np.pi / 180 * x) / (np.cos(np.pi / 180 * x))) for x in range(-360, 361)])
    degrees_in_natural_numbers = np.array([x for x in range(-360, 361)])
#    print("Length of sines array: {}, Length of cosines array: {}, Length of tangents array: {}, Length of N consecutive degrees from -360 to 360: {}".format(len(sines), len(cosines), len(tangents), len(degrees_in_natural_numbers)))
    d = {'sines': sines, 'cosines': cosines, 'tangents': tangents, 'degrees in N': degrees_in_natural_numbers}
    trigonometrical_functions = pd.DataFrame(data=d)
#    print(trigonometrical_functions['sines'][360:480])
    trig_two = trigonometrical_functions
    corr = trig_two.transpose().corr(method='pearson')
    print(corr)
    corr.to_csv('correlation_of_trig_functions_charles_truscott.csv')
    plt.figure(0)
    num = -360
    for x in range(len(corr)):
        plt.plot(corr.loc[x], degrees_in_natural_numbers, label="Degree " + str(num) + "'s correlation with each latter degree")
        num += 1
#    plt.legend(loc='bottom')
    plt.title("Correlation coefficients of minus 360 degrees to positive 360 degrees. Charles Truscott Watters")
    plt.xlabel("Correllation between -360 to 360 degrees of the sine, cosine and tangent to each other degree in the series")
    plt.ylabel("Zero to three-hundred and sixty")
    plt.show()
if __name__ == "__main__": main()
