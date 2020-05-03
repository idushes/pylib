from librosa import load, feature
from wavio import read
from numpy import array
from bearmfcc import process

# получаем массив mfcc c заданной длинной и шагом (frame и step в seconds)
def wav2mfccs(file_path, sample_rate, number_mfcc, frame, step, max_mfcc=300, v2=False, winlength=182, frameshift=182, numfilters=12, lowfreq=50, highfreq=2666):
    if v2:
        y = read(file_path).data.astype(int).flatten()
    else:
        y, _ = load(file_path, sr=sample_rate)
    out_mfcc = []  # Выходной массив, содержащий mfcc исходного файла с шагом step
    length = int(frame * sample_rate)  # установленная длина фреймов (в секундах 0.5 = 500 мс)
    step = int(step * sample_rate)  # Шаг смещения при разборе mfcc (в секундах 0.1 = 100мс)
    i = 0
    while len(y) >= length:  # Проходим весь массив y, пока оставшийся кусочек не станет меньше указанной в параметре max_len длинны
        i = i + 1
        if i >= max_mfcc: break
        section = y[:length]  # Берем начальный кусок длинной length
        section = array(section)  # Переводим в numpy
        if not v2:
            mfcc = feature.mfcc(section, sample_rate, n_mfcc=number_mfcc)
        else:
            mfcc = process(
                inList= list(section),
                sampFreq=sample_rate,
                nCep=number_mfcc,
                winLength=winlength,
                frameShift=frameshift,
                numFilt=numfilters,
                lf=lowfreq,
                hf=highfreq
            )
        out_mfcc.append(mfcc)  # Добавляем в выходной массив out_mfcc значение mfcc текущего куска
        y = y[step:]  # Уменьшаем y на step
    return out_mfcc


# def wav2mfccs():
#
#
# def flac2mfccs(*args):
#     return wav2mfccs(args)