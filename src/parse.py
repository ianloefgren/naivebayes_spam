#!/usr/bin/env python

"""
Script to parse spam and ham corpus.

Author: Ian Loefgren
Date: Feb 19 2018

"""

import re
import email

def load_data():
    # load the spam messages
    with open('../data/spam_2/fn.txt','r') as f:
        lines = f.readlines()
        # print(lines)
        lines = [fn.replace('\n','') for fn in lines]
        lines = ['../data/spam_2/'+fn for fn in lines]
        # print(lines)
        lines = lines[:-2]
        # print(lines)
    spam_likelihood = parse(lines)
    # print(spam_likelihood.keys())

    # load the easy ham messages
    with open('../data/easy_ham/fn.txt','r') as f:
        lines = f.readlines()
        # print(lines)
        lines = [fn.replace('\n','') for fn in lines]
        lines = ['../data/easy_ham/'+fn for fn in lines]
        # print(lines)
        lines = lines[:-2]
        # print(lines)
    easyham_likelihood = parse(lines)
    print(easyham_likelihood.keys())
    

def parse(filenames):
    """
    Get message body text with built-in email module, then split and count
    the frequency of each word.
    """
    freq = {}
    err_count = 0
    load_count = 0
    for fn in filenames:
        try:
            with open(fn,'r') as f:
                msg = email.message_from_file(f)
                if msg.is_multipart():
                    for payload in msg.get_payload():
                        # print(type(payload))
                        words = payload.as_string().split()
                        for word in words:
                            if word in freq:
                                freq[word] += 1
                            else:
                                freq[word] = 1
                else:
                    text = msg.get_payload()
                    words = text.split()
                    # print(type(words))
                    # print(words)
                    # freq = {}
                    for word in words:
                        if word in freq:
                            freq[word] += 1
                        else:
                            freq[word] = 1
                    # print(freq)
            load_count += 1
        except UnicodeDecodeError as e:
            err_count += 1
            # print(e)
    
    print('load count: {}'.format(load_count))
    print('error count: {}'.format(err_count))
    return freq

def label():
    pass

def tests():
    # filename = '../data/easy_ham/01992.a1001b981c9a668d9ecac46c889a5516'
    # parse([filename])
    load_data()
    # with open(filename,'r') as f:
    #     msg = email.message_from_file(f)
    #     if msg.is_multipart():
    #         print('multi true')
    #         for payload in msg.get_payload():
    #             print(payload.get_payload())
    #     else:
    #         print(msg.get_payload())
    #         print(type(msg.get_payload()))

if __name__ == "__main__":
    tests()
