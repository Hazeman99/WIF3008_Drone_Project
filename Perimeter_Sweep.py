import time



def main(billy):



    # Travel to/from starting checkpoint 0 from/to the charging base
    frombase = ["forward", 50, "ccw", 150]
    tobase = ["ccw", 150, "forward", 50]

    # Flight path to Checkpoint 1 to 5 and back to Checkpoint 0 sequentially
    checkpoint = [[1, "cw", 90, "forward", 100], [2, "ccw", 90, "forward", 80], [3, "ccw", 90, "forward", 40],
                  [4, "ccw", 90, "forward", 40], [5, "cw", 90, "forward", 60], [0, "ccw", 90, "forward", 40]]


    if not billy.get_isSecondSweep:
        # Put Tello into command mode
        if billy.get_interrupt_status():
            print("Interrupt - Manual Control On!")
            return

        billy.send_command("command", 3)

    # Send the takeoff command
    if billy.get_interrupt_status():
        print("Interrupt - Manual Control On!")
        return

    if not billy.get_isSecondSweep:
        billy.send_command("takeoff", 7)

    print("\n")

    # Start at checkpoint 1 and print destination
    if not billy.get_isSecondSweep:
        print("From the charging base to the starting checkpoint of sweep pattern.\n")
    
    if billy.get_interrupt_status():
        print("Interrupt - Manual Control On!")
        return

    if not billy.get_isSecondSweep:
        billy.send_command(frombase[0] + " " + str(frombase[1]), 4)
        billy.send_command(frombase[2] + " " + str(frombase[3]), 4)
        print("Current location: Checkpoint 0 " + "\n")

    if billy.get_isSecondSweep():
        # Billy's flight path
        print("Continuing Perimeter Sweep. \n")
        print("Current location: Checkpoint " + str(billy.get_second_sweep_index()) + "\n")

        for i in range(billy.get_second_sweep_index(), len(checkpoint)):
            if billy.get_interrupt_status():
                billy.set_isSecondSweep(True)
                billy.set_second_sweep_index(i);
                print("Interrupt - Manual Control On!")
                return
            if i == len(checkpoint)-1:
                print("Returning to Checkpoint 0. \n")

            billy.send_command(checkpoint[i][1] + " " + str(checkpoint[i][2]), 4)
            billy.send_command(checkpoint[i][3] + " " + str(checkpoint[i][4]), 4)

            print("Arrived at current location: Checkpoint " +
                str(checkpoint[i][0]) + "\n")
            time.sleep(4)
    else:
        # Billy's flight path
        for i in range(len(checkpoint)):
            if billy.get_interrupt_status():
                billy.set_isSecondSweep(True)
                billy.set_second_sweep_index(i);
                print("Interrupt - Manual Control On!")
                return
            if i == len(checkpoint)-1:
                print("Returning to Checkpoint 0. \n")

            billy.send_command(checkpoint[i][1] + " " + str(checkpoint[i][2]), 4)
            billy.send_command(checkpoint[i][3] + " " + str(checkpoint[i][4]), 4)

            print("Arrived at current location: Checkpoint " +
                str(checkpoint[i][0]) + "\n")
            time.sleep(4)
    

    # Reach back at Checkpoint 0
    print("Complete sweep. Return to charging base.\n")
    if billy.get_interrupt_status():
        print("Interrupt - Manual Control On!")
        return

    billy.send_command(tobase[0] + " " + str(tobase[1]), 4)
    billy.send_command(tobase[2] + " " + str(tobase[3]), 4)


    # Turn to original direction before land
    print("Turn to original direction before land.\n")
    if billy.get_interrupt_status():
        print("Interrupt - Manual Control On!")
        return

    billy.send_command("cw 180", 4)

    # Land
    if billy.get_interrupt_status():
        print("Interrupt - Manual Control On!")
        return
    billy.send_command("land", 3)



if __name__ == "__main__":
    main()
