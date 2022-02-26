import pandas as pd
import shutil
import os

PATH = "Dataset/"
OLD_NOISY_PATH = PATH + "noisy_trainset_wav/"
OLD_CLEAN_PATH = PATH + "clean_trainset_wav/"

NEW_NOISY_PATH = PATH + "noisy_valset_wav/"
NEW_CLEAN_PATH = PATH + "clean_valset_wav/"

classes = [
    "kitchen",
    "cafeteria",
    "traffic",
    "meeting",
    "ssn",
    "station",
    "car",
    "metro",
    "restaurant",
    "babble"
]

db_levels = [0, 5, 10, 15]


def create_samples(samples, db, cl, quantity):
    cont = (samples[2] == db)
    samples = samples[cont]
    cont = (samples[1] == cl)
    samples = samples[cont].sample(n=quantity)
    return samples


def get_db_samples_from_txt(temp_db0, temp_db5, temp_db10, temp_db15, samples):
    for di in range(0, len(db_levels)):
        for ci in range(0, len(classes)):
            temp_sample = create_samples(samples, db_levels[di], classes[ci], 8)

            if di == 0:
                temp_db0 = pd.concat([temp_db0, temp_sample])
            elif di == 1:
                temp_db5 = pd.concat([temp_db5, temp_sample])
            elif di == 2:
                temp_db10 = pd.concat([temp_db10, temp_sample])
            else:
                temp_db15 = pd.concat([temp_db15, temp_sample])
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

    dB0 = pd.DataFrame()
    dB5 = pd.DataFrame()
    dB10 = pd.DataFrame()
    dB15 = pd.DataFrame()

    data = pd.read_csv(PATH + log_file, sep=" ", header=None)

    dB0, dB5, dB10, dB15 = get_db_samples_from_txt(dB0, dB5, dB10, dB15, data)

    copy_files(dB0, dB5, dB10, dB15)
    write_excel(dB0, dB5, dB10, dB15)

