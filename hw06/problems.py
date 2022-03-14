import re

def problem1(searchstring):
    """
    Match phone numbers.

    :param searchstring: string
    :return: True or False
    """
    """
    valid format: 
    +1 (XXX) XXX-XXXX
    +1 XXX-XXX-XXXX
    +1 XXXXXXXXXX
    """
    #if(re.search('^(+1|+52)', searchstring) and re.search(' $', searchstring)):
    if(re.search('^ ', searchstring) or re.search(' $', searchstring)):
        return False
    if searchstring.startswith('+1') or searchstring.startswith('+52'):
        pattern1 = '\(\d{3}\)\s*\d{3}-\d{4}'  #+1/52 (XXX) XXX-XXXX
        pattern2 = '\d{3}-\d{3}-\d{4}'        #+1/52 XXX-XXX-XXXX
        pattern3 = '\d{3}\d{3}\d{4}'          #+1/52 XXXXXXXXXX
        
        if(re.search('^ ', searchstring) or re.search(' $', searchstring)):
            return False
        if re.search(pattern1, searchstring):
            return True
        elif re.search(pattern2, searchstring):
            return True
        elif re.search(pattern3, searchstring):
            return True
        else:
            return False
    else:
        patternNoCountry = '\d{3}-\d{4}'
        if(re.fullmatch(patternNoCountry, searchstring)):
            return True
        else:
            return False
            
def problem2(searchstring):
    """
    Extract street name from address.

    :param searchstring: string
    :return: string
    """
    pattern = '\d+\s[A-Z](.*?)(Rd|Ave|St|Dr)\.'
    endpoint = re.search(pattern, searchstring).group()
    #print(endpoint)
    search_num = re.search(r'\d+', endpoint[::-1]).group()[::-1]
    split_string = endpoint.partition(search_num)[1]+endpoint.partition(search_num)[2]
    roadType = re.search(r"\s(Rd|Ave|St|Dr)\.", split_string).group()
    deleteRoadType = split_string.partition(roadType)[0]
    #print(deleteRoadType)
    return deleteRoadType

def problem3(searchstring):
    """
    Garble Street name.

    :param searchstring: string
    :return: string
    """
    split_string = searchstring.partition('.')
    before1dot = split_string[0] + '.'
    #print(before1dot)
    doorNum = re.findall(r'\d+', before1dot)[-1]    #find door number, return type str
    split_string2 = searchstring.partition(doorNum)
    #print(split_string2)
    string_after_digit = split_string2[2]
    findStreetName = re.search('\s*(.*?)\s*(Rd|Ave|St|Dr)\.', string_after_digit)
    streetName = findStreetName.group(1)
    #print(streetName)
    reversedStreetName = streetName[::-1]
    newString = re.sub(streetName, reversedStreetName, string_after_digit)
    newnewString = re.sub(string_after_digit, newString, searchstring)
    #print(newnewString)
    return newnewString


if __name__ == '__main__' :
    print("\nProblem 1:")
    print("Answer correct?", problem1('+1 765-494-4600') == True)
    print("Answer correct?", problem1('+52 765-494-4600 ') == False)
    print("Answer correct?", problem1('+1 (765) 494 4600') == False)
    print("Answer correct?", problem1('+52 (765) 494-4600') == True)
    print("Answer correct?", problem1('+52 7654944600') == True)
    print("Answer correct?", problem1('494-4600') == True)

    print("\nProblem 2:")
    print("Answer correct?",problem2('1 abc St. 1 Abc St.') == "1 Abc")
    print("Answer correct?",problem2('Meet me at 201 South First St. at noon') == "201 South First")
    print("Answer correct?",problem2('Type "404 Not Found St" on your phone at 201 South First St. at noon') == "201 South First")
    print("Answer correct?",problem2("123 Mayb3 Y0u 222 Did not th1nk 333 This Through Rd. Did Y0u Ave.") == "333 This Through")
    
    print("\nProblem 3:")
    print("Answer correct?",problem3('Go West on 999 West St.') == "Go West on 999 tseW St.")
    print("Answer correct?",problem3('Meet me at 201 South First St. at noon') == "Meet me at 201 tsriF htuoS St. at noon")