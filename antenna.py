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

# The functions below are adapted from examples by user junglejet,
# "How to save a dictionary to a file?" Stack Overflow,
# https://stackoverflow.com/questions/19201290/how-to-save-a-dictionary-to-a-file,
# CC-BY-SA 4.0.

def save_dict_to_file(dic):
    f = open(os.path.join(os.path.expanduser('~'), '.local', 'share', 'antenna', 'antennarc'),'w')
    f.write(str(dic))
    f.close()

def load_dict_from_file():
    f = open(os.path.join(os.path.expanduser('~'), '.local', 'share', 'antenna', 'antennarc'),'r')
    data=f.read()
    f.close()
    return eval(data)

# End of code adapted from examples by user junglejet.

def main_menu():
    if os.path.isfile(os.path.join(os.path.expanduser('~'), '.local', 'share', 'antenna', 'antennarc'))==False:
        if os.path.isdir(os.path.join(os.path.expanduser('~'), '.local', 'share', 'antenna'))==False:
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
            print()
            exit()
        elif menu_user_choice == "a":
            add_station(station_list)
        elif menu_user_choice == "d":
            input_error_filter("delete", station_list)
        elif menu_user_choice == "e":
            input_error_filter("edit", station_list)
        elif menu_user_choice == "m":
            input_error_filter("move", station_list)
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

def station_display(station_list):
    os.system('clear')
    print()
    print("Antenna - Internet Radio Player")
    print("===============================")
    print()
    print("Station List:")
    print()
    total_entries = int(len(station_list))
    if total_entries <= 12:
        for i in station_list:
            print(i,station_list[i]['Name'])
    if total_entries > 12:
        col1 = 1
        col2 = int(total_entries/2) + total_entries%2 + 1
        rows = int(total_entries/2) + total_entries%2
        for i in range (0, rows):
            if col1 < rows:
                print(f"{str(col1) + ' ' + station_list[col1]['Name']:<30}{str(col2) + ' ' + station_list[col2]['Name']}")
            if col1 == rows and col2 > total_entries:
                print(col1, station_list[col1]['Name'])
            if col1 == rows and col2 == total_entries:
                print(f"{str(col1) + ' ' + station_list[col1]['Name']:<30}{str(col2) + ' ' + station_list[col2]['Name']}")
            col1 = col1 + 1
            col2 = col2 + 1
    print()

def input_error_filter (action, station_list):
    print()
    user_choice = input(f"Enter the number of the station to {action}: ")

    if user_choice.isnumeric() == False:
        input_error_message()

    user_choice_integer = int(user_choice)
    total_entries = len(station_list)

    if user_choice_integer < 1 or user_choice_integer > total_entries:
        input_error_message()

    eval(action+"_station")(station_list, user_choice_integer, total_entries) #this calls a function using a variable: eval(action+"_station") produces the function name.

def input_error_message():
    print()
    print("Invalid Entry - Returning to Main Menu")
    time.sleep(1)
    main_menu()

def add_station(station_list):
    print()
    new_station_URL = input("Enter the station URL: ")
    print()
    new_station_name = input("Enter the station name: ")
    new_station = {len(station_list)+1: {'Name': new_station_name, 'sURL': new_station_URL}}
    save_dict_to_file(station_list | new_station)
    main_menu()

def delete_station(station_list, user_choice_integer, total_entries):

    new_station_list = {}
    for i in station_list:
        if i < user_choice_integer:
            new_station_list[i] = {'Name': station_list[i]['Name'], 'sURL': station_list[i]['sURL']}
        if i > user_choice_integer:
            new_station_list[i-1] = {'Name': station_list[i]['Name'], 'sURL': station_list[i]['sURL']}
    save_dict_to_file(new_station_list)
    main_menu()

def edit_station(station_list, user_choice_integer, total_entries): # total_entries is not used in this function, but the generic call from station_filter() requires it.
    print()
    print("The current station name is:", station_list[user_choice_integer]['Name'])
    print()
    edited_name = input("Enter a new name or leave blank to keep the current entry: ")
    if edited_name != "":
        edited_name_value={'Name':edited_name}
        station_list[user_choice_integer].update(edited_name_value)
        save_dict_to_file(station_list)
    print()
    print("The current station URL is:", station_list[user_choice_integer]['sURL'])
    print()
    edited_URL = input("Enter a new URL or leave blank to keep the current entry: ")
    if edited_URL != "":
        edited_URL_value={'sURL':edited_URL}
        station_list[user_choice_integer].update(edited_URL_value)
        save_dict_to_file(station_list)
    main_menu()

def move_station (station_list, user_choice_integer, total_entries):
    station_display(station_list)
    print("Command Menu:")
    print()
    print("u move the station up")
    print("d move the station down")
    print("q return to the main menu")
    print()
    station_movement = input("Enter your selection: ")

    if station_movement.isnumeric() == True:
        move_station(station_list, user_choice_integer, total_entries)

    elif station_movement == "q":
        main_menu()

    elif station_movement == "u":
        if user_choice_integer == 1:
            print()
            print("The station is already at the first position.")
            time.sleep(1)
            move_station(station_list, user_choice_integer, total_entries)
        new_station_list = {}
        merged_station_list = {}
        new_station_list[user_choice_integer-1] = {'Name': station_list[user_choice_integer]['Name'], 'sURL': station_list[user_choice_integer]['sURL']}
        new_station_list[user_choice_integer] = {'Name': station_list[user_choice_integer-1]['Name'], 'sURL': station_list[user_choice_integer-1]['sURL']}
        merged_station_list = station_list | new_station_list
        save_dict_to_file(merged_station_list)
        user_choice_integer=user_choice_integer-1
        move_station(merged_station_list, user_choice_integer, total_entries)

    elif station_movement == "d":
        if user_choice_integer == total_entries:
            print()
            print("The station is already at last position.")
            time.sleep(1)
            move_station(station_list, user_choice_integer, total_entries)
        new_station_list = {}
        merged_station_list = {}
        new_station_list[user_choice_integer+1] = {'Name': station_list[user_choice_integer]['Name'], 'sURL': station_list[user_choice_integer]['sURL']}
        new_station_list[user_choice_integer] = {'Name': station_list[user_choice_integer+1]['Name'], 'sURL': station_list[user_choice_integer+1]['sURL']}
        merged_station_list = station_list | new_station_list
        save_dict_to_file(merged_station_list)
        user_choice_integer=user_choice_integer+1
        move_station(merged_station_list, user_choice_integer, total_entries)

    else:
        move_station(station_list, user_choice_integer, total_entries)

def play_stream(stream_url):
    print()
    print("Press 'q' to stop playback ")
    os.system(f'gst123 -q {stream_url}')
    main_menu()

main_menu()
