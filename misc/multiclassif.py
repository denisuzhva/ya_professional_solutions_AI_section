import random



n_classifs = 5
classif_acc = 0.6

def randBool(prob):
    return random.random() < prob

def emulateEpoch():
    label = randBool(0.5)
    spams = 0
    nospams = 0
    for _ in range(n_classifs):
        isright = randBool(classif_acc)
        if isright:
            if label:
                spams += 1
            else:
                nospams += 1
        else:
            if label:
                nospams += 1
            else:
                spams += 1
    if spams > nospams:
        return True
    else:
        return False

if __name__ == '__main__':
    epochs = 1000000
    tpfn = 0.0
    for _ in range(epochs):
        tpfn += 1 if emulateEpoch() else 0

    acc = tpfn / epochs
    print('Accuracy: %f' % acc)


