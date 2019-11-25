import numpy as np
from turtle import Screen, Turtle



hilbert_sequence = ""

def checkSequence(seq, lab):
    s_pos_data = np.where(lab == 0)
    num_s_pos = s_pos_data[0].shape[0]
    num_good_s_pos = 0
    for s_pos_iter in range(num_s_pos):
        current_row = s_pos_data[0][s_pos_iter]
        current_col = s_pos_data[1][s_pos_iter]
        #print('%i %i' % (current_row, current_col))
        for com_msg in seq:
            if com_msg == 'D':
                if lab[current_row+1][current_col] == 0:
                    current_row += 1
                elif lab[current_row+1][current_col] == 9:
                    num_good_s_pos += 1
                    break
            if com_msg == 'U':
                if lab[current_row-1][current_col] == 0:
                    current_row -= 1
                elif lab[current_row-1][current_col] == 9:
                    num_good_s_pos += 1
                    break
            if com_msg == 'R':
                if lab[current_row][current_col+1] == 0:
                    current_col += 1
                elif lab[current_row][current_col+1] == 9:
                    num_good_s_pos += 1
                    break
            if com_msg == 'L':
                if lab[current_row][current_col-1] == 0:
                    current_col -= 1
                elif lab[current_row][current_col-1] == 9:
                    num_good_s_pos += 1
                    break
    print(num_good_s_pos)
    if num_good_s_pos == num_s_pos:
        return True
    else:
        return False


def hilbertCurve(turtle, A, parity, n):
    if n < 1:
        return
    global hilbert_sequence
    turtle.left(parity * 90)
    hilbertCurve(turtle, A, - parity, n - 1)
    turtle.forward(A)
    hdn = turtle.heading()
    if hdn == 0.0:
        hilbert_sequence += "R"
    if hdn == 90.0:
        hilbert_sequence += "U"
    if hdn == 180.0:
        hilbert_sequence += "L"
    if hdn == 270.0:
        hilbert_sequence += "D"

    turtle.right(parity * 90)
    hilbertCurve(turtle, A, parity, n - 1)
    turtle.forward(A)
    hdn = turtle.heading()
    if hdn == 0.0:
        hilbert_sequence += "R"
    if hdn == 90.0:
        hilbert_sequence += "U"
    if hdn == 180.0:
        hilbert_sequence += "L"
    if hdn == 270.0:
        hilbert_sequence += "D"

    hilbertCurve(turtle, A, parity, n - 1)
    turtle.right(parity * 90)
    turtle.forward(A)
    hdn = turtle.heading()
    if hdn == 0.0:
        hilbert_sequence += "R"
    if hdn == 90.0:
        hilbert_sequence += "U"
    if hdn == 180.0:
        hilbert_sequence += "L"
    if hdn == 270.0:
        hilbert_sequence += "D"

    hilbertCurve(turtle, A, - parity, n - 1)
    turtle.left(parity * 90)
    


if __name__ == '__main__':
    lab = np.genfromtxt('./lab.txt', delimiter=[1,1,1,1,1,1,1,1,1,1])
    lab_padded = np.ones((12, 12))
    lab_padded[1:-1, 1:-1] = lab
    exit_coord = [np.where(lab_padded==9)[0][0], np.where(lab_padded==9)[1][0]]
    print(exit_coord)
    print(lab_padded)

    sample_seq = 'URDRUUULDLUUURDRURDRURDDDLULDDDRURD'


    screen = Screen()
    yertle = Turtle()
    yertle.speed('fastest')  # because I have no patience
    #hilbertCurve(yertle, 10, 1, 5)
    #screen.exitonclick()

    hilbert_sequence = "URDRRULURULLDLUURULUURDRURDDLDRRRULUURDRURDDLDRDDLULLDRDLDRRURDRRULUURDRURDDLDRRURDRRULURULLDLUUURDRRULURULLDLULLDRDDLULDLUURULURULUURDRURDDLDRRURDRRULURULLDLUUURDRRULURULLDLULLDRDDLULDLUURULLDLULLDRDLDRRURDDLDRDDLULDLUURULLLDRDDLULDLUURULUURDRRULURULLDLUURULUURDRURDDLDRRURDRRULURULLDLUUURDRRULURULLDLULLDRDDLULDLUURULUURDRRULURULLDLUURULUURDRURDDLDRRRULUURDRURDDLDRDDLULLDRDLDRRURDRURDRRULURULLDLUURULUURDRURDDLDRRRULUURDRURDDLDRDDLULLDRDLDRRURDDLDRDDLULDLUURULLDLULLDRDLDRRURDDDLULLDRDLDRRURDRRULUURDRURDDLDRRRULUURDRURDDLDRRURDRRULURULLDLUUURDRRULURULLDLULLDRDDLULDLUURULUURDRRULURULLDLUURULUURDRURDDLDRRRULUURDRURDDLDRDDLULLDRDLDRRURDRURDRRULURULLDLUURULUURDRURDDLDRRRULUURDRURDDLDRDDLULLDRDLDRRURDDLDRDDLULDLUURULLDLULLDRDLDRRURDDDLULLDRDLDRRURDRRULUURDRURDDLDRDDLULLDRDLDRRURDDLDRDDLULDLUURULLLDRDDLULDLUURULUURDRRULURULLDLULLDRDDLULDLUURULLDLULLDRDLDRRURDDDLULLDRDLDRRURDRRULUURDRURDDLDRDLDRDDLULDLUURULLDLULLDRDLDRRURDDDLULLDRDLDRRURDRRULUURDRURDDLDRRURDRRULURULLDLU"
    hilbert_sequence = "URDRRULURULLDLUURULUURDRURDDLDRRRULUURDRURDDLDRDDLULLDRDLDRRURDRRULUURDRURDDLDRRURDRRULURULLDLUUURDRRULURULLDLULLDRDDLULDLUURULURULUURDRURDDLDRRURDRRULURULLDLUUURDRRULURULLDLULLDRDDLULDLUURULLDLULLDRDLDRRURDDLDRDDLULDLUURULLLDRDDLULDLUURULUURDRRULURULLDLUURULUURDRURDDLDRRURDRRULURULLDLUUURDRRULURULLDLULLDRDDLULDLUURULUURDRRULURULLDLUURULUURDRURDDLDRRRULUURDRURDDLDRDDLULLDRDLDRRURDRURDRRULURULLDLUURULUURDRURDDLDRRRULUURDRURDDLDRDDLULLDRDLDRRURDDLDRDDLULDLUURULLDLULLDRDLDRRURDDDLULLDRDLDRRURDRRULUURDRURDDLDRRRULUURDRURDDLDRRURDRRULURULLDLUUURDRRULURULLDLULLDRDDLULDLUURULUURDRRULURULLDLUURULUURDRURDDLDRRRULUURDRURDDLDRDDLULLDRDLDRRURDRURDRRULURULLDLUURULUURDRURDDLDRRRULUURDRURDDLDRDDLULLDRDLDRRURDDLDRDDLULDLUURULLDLULLDRDLDRRURDDDLULLDRDLDRRURDRRULUURDRURDDLDRDDLULLDRDLDRRURDDLDRDDLULDLUURULLLDRDDLULDLUURULUURDRRULURULLDLULLDRDDLULDLUURULLDLULLDRDLDRRURDDDLULLDRDLDRRURDRRULUURDRURDDLDRDLDRDDLULDLUURULLDLULLDRDLDRRURDDDLULLDRDLDRRURDRRULUURDRURDDLDRRURDRRULURULLDLU"
    print(hilbert_sequence)
    print(len(hilbert_sequence))


    ## Check it
    answer = checkSequence(hilbert_sequence, lab_padded)
    print(answer)


