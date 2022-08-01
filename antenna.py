#!/usr/bin/env python3

#    Antenna - an internet radio stream player.
#    Copyright (C) 2022 Visiblink
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import time
from sys import exit

# The functions below are by user junglejet, "How to save a dictionary to a file?" Stack Overflow,
# https://stackoverflow.com/questions/19201290/how-to-save-a-dictionary-to-a-file, CC-BY-SA 4.0.

def save_dict_to_file(dic):
    f = open(os.path.join(os.path.expanduser('~'), '.local', 'share', 'antenna', 'antennarc'),'w')
    f.write(str(dic))
    f.close()

def load_dict_from_file():
    f = open(os.path.join(os.path.expanduser('~'), '.local', 'share', 'antenna', 'antennarc'),'r')
    data=f.read()
    f.close()
    return eval(data)

# End of code by user junglejet.

def add_station(internal_station_list):
    print()
    new_station_URL = input("Enter the station URL: ")
    print()
    new_station_name = input("Enter the station name: ")
    new_station = {len(internal_station_list)+1: {'Name': new_station_name, 'sURL': new_station_URL}}
    save_dict_to_file(internal_station_list | new_station)
    main_menu()

def delete_station(internal_station_list):
    print()
    user_choice = input("Enter the number of the station to delete: ")
    if user_choice.isnumeric() == False:
        print()
        print("Invalid Entry - Returning to Main Menu")
        time.sleep(1)
        main_menu()

    else:
        # set counters
        user_choice_integer = int(user_choice)
        total_entries = len(internal_station_list)

        if user_choice_integer < 1 or user_choice_integer > total_entries:
            print()
            print("Invalid Entry - Returning to Main Menu")
            time.sleep(1)
            main_menu()

        # delete entry if it's the last entry and return to main menu
        elif user_choice_integer == total_entries:
            del internal_station_list[user_choice_integer]
            save_dict_to_file(internal_station_list)
            main_menu()

        else:
            del internal_station_list[int(user_choice)] # delete the selected station
            new_station_list={} # create new dictionary
            # transfer stations from 1 to the number before the deletion to the new dictionary
            for i in internal_station_list:
                if i < user_choice_integer:
                    new_station_list[i] = {'Name': internal_station_list[i]['Name'], 'sURL': internal_station_list[i]['sURL']}

            # renumber stations after the deletion down by one in the new dictionary and save to file
            for i in internal_station_list:
                user_choice_integer=user_choice_integer+1
                new_station_list[user_choice_integer-1] = {'Name': internal_station_list[user_choice_integer]['Name'], 'sURL': internal_station_list[user_choice_integer]['sURL']}
                if user_choice_integer == total_entries:
                    save_dict_to_file(new_station_list)
                    main_menu()

def edit_station_name(internal_station_list):
    print()
    user_choice = input("Enter the number of the station to edit: ")

    if user_choice.isnumeric() == False:
        print()
        print("Invalid Entry - Returning to Main Menu")
        time.sleep(1)
        main_menu()

    user_choice_integer = int(user_choice)
    total_entries = len(internal_station_list)

    if user_choice_integer < 1 or user_choice_integer > total_entries:
        print()
        print("Invalid Entry - Returning to Main Menu")
        time.sleep(1)
        main_menu()

    print()
    print("The current station name is:", internal_station_list[user_choice_integer]['Name'])
    print()
    edited_name = input("Enter a new name or leave blank to keep the current entry: ")
    if edited_name == "":
        edit_station_URL(internal_station_list, user_choice_integer)
    else:
        edited_name_value={'Name':edited_name}
        internal_station_list[user_choice_integer].update(edited_name_value)
        save_dict_to_file(internal_station_list)
        edit_station_URL(internal_station_list, user_choice_integer)

def edit_station_URL(internal_station_list, user_choice_integer):
    print()
    print("The current station URL is:", internal_station_list[user_choice_integer]['sURL'])
    print()
    edited_URL = input("Enter a new URL or leave blank to keep the current entry: ")
    if edited_URL == "":
        main_menu()
    else:
        edited_URL_value={'sURL':edited_URL}
        internal_station_list[user_choice_integer].update(edited_URL_value)
        print(internal_station_list)
        save_dict_to_file(internal_station_list)
        main_menu()

def move_station_filter (internal_station_list):
    print()
    user_choice = input("Enter the number of the station to move: ")

    if user_choice.isnumeric() == False:
        print()
        print("Invalid Entry - Returning to Main Menu")
        time.sleep(1)
        main_menu()

    user_choice_integer = int(user_choice)
    total_entries = len(internal_station_list)

    if user_choice_integer < 1 or user_choice_integer > total_entries:
        print()
        print("Invalid Entry - Returning to Main Menu")
        time.sleep(1)
        main_menu()

    move_station(internal_station_list, user_choice_integer)

def move_station (internal_station_list, user_choice_integer):
    station_display(internal_station_list)
    print("Command Menu:")
    print()
    print("u move the station up")
    print("d move the station down")
    print("m return to the main menu")
    print()
    station_movement = input("Enter your selection: ")

    total_entries = len(internal_station_list)

    if station_movement.isnumeric() == True:
        move_station(internal_station_list, user_choice_integer)

    elif station_movement == "m":
        main_menu()

    elif station_movement == "u":
        if user_choice_integer == 1:
            print()
            print("The station is already at the first position.")
            time.sleep(1)
            move_station(internal_station_list, user_choice_integer)
        new_station_list = {}
        merged_station_list = {}
        new_station_list[user_choice_integer-1] = {'Name': internal_station_list[user_choice_integer]['Name'], 'sURL': internal_station_list[user_choice_integer]['sURL']}
        new_station_list[user_choice_integer] = {'Name': internal_station_list[user_choice_integer-1]['Name'], 'sURL': internal_station_list[user_choice_integer-1]['sURL']}
        merged_station_list = internal_station_list | new_station_list
        save_dict_to_file(merged_station_list)
        user_choice_integer=user_choice_integer-1
        move_station(merged_station_list, user_choice_integer)

    elif station_movement == "d":
        if user_choice_integer == total_entries:
            print()
            print("The station is already at last position.")
            time.sleep(1)
            move_station(internal_station_list, user_choice_integer)
        new_station_list = {}
        merged_station_list = {}
        new_station_list[user_choice_integer+1] = {'Name': internal_station_list[user_choice_integer]['Name'], 'sURL': internal_station_list[user_choice_integer]['sURL']}
        new_station_list[user_choice_integer] = {'Name': internal_station_list[user_choice_integer+1]['Name'], 'sURL': internal_station_list[user_choice_integer+1]['sURL']}
        merged_station_list = internal_station_list | new_station_list
        save_dict_to_file(merged_station_list)
        user_choice_integer=user_choice_integer+1
        move_station(merged_station_list, user_choice_integer)

    else:
        move_station(internal_station_list, user_choice_integer)

def play_stream(stream_url):
    print()
    print("Press 'q' to stop playback ")
    os.system(f'gst123 -q {stream_url}')
    main_menu()

def station_display(internal_station_list):
    os.system('clear')
    print()
    print("Antenna - Internet Radio Player")
    print("===============================")
    print()
    print("Station List:")
    print()
    total_entries = int(len(internal_station_list))
    if total_entries <= 12:
        for i in internal_station_list:
            print(i,internal_station_list[i]['Name'])
    if total_entries > 12:
        col1 = 1
        col2 = int(total_entries/2) + total_entries%2 + 1
        rows = int(total_entries/2) + total_entries%2
        for i in range (0, rows):
            if col1 < rows:
                print(f"{str(col1) + ' ' + internal_station_list[col1]['Name']:<30}{str(col2) + ' ' + internal_station_list[col2]['Name']}")
            if col1 == rows and col2 > total_entries:
                print(col1, internal_station_list[col1]['Name'])
            if col1 == rows and col2 == total_entries:
                print(f"{str(col1) + ' ' + internal_station_list[col1]['Name']:<30}{str(col2) + ' ' + internal_station_list[col2]['Name']}")
            col1 = col1 + 1
            col2 = col2 + 1
    print()

def main_menu():
    if os.path.isfile(os.path.join(os.path.expanduser('~'), '.local', 'share', 'antenna', 'antennarc'))==False:
        if os.path.isdir(os.path.join(os.path.expanduser('~'), '.local', 'share', 'antenna', 'antennarc'))==False:
            os.mkdir(os.path.join(os.path.expanduser('~'), '.local', 'share', 'antenna'))
        station_list={}
    else:
        station_list = load_dict_from_file()
    station_display(station_list)
    print("Command Menu:")
    print()
    print("a add a station shortcut")
    print("d delete a station shortcut")
    print("e edit a station shortcut")
    print("m move a station shortcut up or down")
    print("p play a manually entered URL")
    print("q exit")
    print()
    menu_user_choice = input("Enter the number or letter of your selection: ")
    if menu_user_choice.isnumeric() == False:
        if menu_user_choice == "q":
            exit()
        elif menu_user_choice == "a":
            add_station(station_list)
        elif menu_user_choice == "d":
            delete_station(station_list)
        elif menu_user_choice == "e":
            edit_station_name(station_list)
        elif menu_user_choice == "m":
            move_station_filter(station_list)
        elif menu_user_choice == "p":
            print()
            user_stream_url = input("Enter the stream URL: ")
            play_stream(user_stream_url)
        else:
            main_menu()
    elif int(menu_user_choice) == 0:
        main_menu()
    elif int(menu_user_choice) <= len(station_list):
        print()
        print("Now Playing -", station_list[int(menu_user_choice)]['Name'])
        play_stream(station_list[int(menu_user_choice)]['sURL'])
    else:
        main_menu()

main_menu()
