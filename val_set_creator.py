import pandas as pd
import shutil
import os

PATH = "Dataset/"
OLD_NOISY_PATH = PATH + "noisy_trainset_wav/"
OLD_CLEAN_PATH = PATH + "clean_trainset_wav/"

NEW_NOISY_PATH = PATH + "noisy_valset_wav/"
NEW_CLEAN_PATH = PATH + "clean_valset_wav/"


def get_sample_from_txt(samples):
    cont = (samples[2] == 0)
    temp_db0 = samples[cont].sample(n=75)
    cont = (samples[2] == 5)
    temp_db5 = samples[cont].sample(n=75)
    cont = (samples[2] == 10)
    temp_db10 = samples[cont].sample(n=75)
    cont = (samples[2] == 15)
    temp_db15 = samples[cont].sample(n=75)

    return temp_db0, temp_db5, temp_db10, temp_db15


def write_excel(temp_db0, temp_db5, temp_db10, temp_db15):
    with pd.ExcelWriter(PATH + "valset_log.xlsx") as writer:
        temp_db0.to_excel(writer, sheet_name="dB0")
        temp_db5.to_excel(writer, sheet_name="dB5")
        temp_db10.to_excel(writer, sheet_name="dB10")
        temp_db15.to_excel(writer, sheet_name="dB15")


def copy_files(temp_db0, temp_db5, temp_db10, temp_db15):

    if not os.path.exists(NEW_NOISY_PATH):
        os.makedirs(NEW_NOISY_PATH)

    if not os.path.exists(NEW_CLEAN_PATH):
        os.makedirs(NEW_CLEAN_PATH)

    for x in temp_db0[0]:
        shutil.move(OLD_NOISY_PATH + x + ".wav", NEW_NOISY_PATH + x + ".wav")
        shutil.move(OLD_CLEAN_PATH + x + ".wav", NEW_CLEAN_PATH + x + ".wav")
    for x in temp_db5[0]:
        shutil.move(OLD_NOISY_PATH + x + ".wav", NEW_NOISY_PATH + x + ".wav")
        shutil.move(OLD_CLEAN_PATH + x + ".wav", NEW_CLEAN_PATH + x + ".wav")
    for x in temp_db10[0]:
        shutil.move(OLD_NOISY_PATH + x + ".wav", NEW_NOISY_PATH + x + ".wav")
        shutil.move(OLD_CLEAN_PATH + x + ".wav", NEW_CLEAN_PATH + x + ".wav")
    for x in temp_db15[0]:
        shutil.move(OLD_NOISY_PATH + x + ".wav", NEW_NOISY_PATH + x + ".wav")
        shutil.move(OLD_CLEAN_PATH + x + ".wav", NEW_CLEAN_PATH + x + ".wav")

if __name__ == '__main__':
    log_file = "/log_trainset_28spk.txt"

    data = pd.read_csv(PATH + log_file, sep=" ", header=None)

    dB0, dB5, dB10, dB15 = get_sample_from_txt(data)
    write_excel(dB0, dB5, dB10, dB15)
    copy_files(dB0, dB5, dB10, dB15)
