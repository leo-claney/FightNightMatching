#Take in the rankings of each auditionee, each group, and the maximum number of people each group would take 
#NOTE - The maximum number of people in each group is fairly important for this
#TODO - Strip whitespaces
import csv
class Auditionee:
    def __init__(self, name: str, rankings: list):
        self.name = name
        self.rankings = rankings
        self.group = None

class Group:
    def __init__(self, name: str, rankings: list, maxCap: int):
        self.name = name
        self.rankings = rankings
        self.groupMax = maxCap
        self.newMembers = []
                    
def auditioneematcher(groups: list, auditionees: list):
    for group in groups:
        for auditioneeNames in group.rankings:
            for auditionee in auditionees:
                if auditionee.name == auditioneeNames:
                    if auditionee.group == None:
                        auditionee.group = group
                        group.newMembers.append(auditionee)
                    else:
                        if auditionee.rankings.index(group.name) < auditionee.rankings.index(auditionee.group.name):
                            auditionee.group.newMembers.remove(auditionee)
                            auditionee.group = group
                            group.newMembers.append(auditionee)

def allGroupsFull(groups: list):
    for group in groups:
        if len(group.newMembers) < group.groupMax:
            return False
    return True

def groupmatcher(groups: list, auditionees: list):
    while not allGroupsFull(groups):
        for auditionee in auditionees:
            for groupName in auditionee.rankings:
                if auditionee.group == None:
                    for group in groups:
                        if group.name == groupName:
                            if auditionee.name in group.rankings:
                                if len(group.newMembers) < group.groupMax:
                                    auditionee.group = group
                                    group.newMembers.append(auditionee)
                                else:
                                    # if auditionee.group == None:
                                    lowMember = group.newMembers[0]
                                    for member in group.newMembers:
                                        if group.rankings.index(member.name) > group.rankings.index(lowMember.name):
                                            lowMember = member
                                    if group.rankings.index(auditionee.name) < group.rankings.index(lowMember.name):
                                        lowMember.group = None
                                        group.newMembers.remove(lowMember)
                                        auditionee.group = group
                                        group.newMembers.append(auditionee)



def test_csv():
    with open('Fight Night Rankings - Test Group Rankings.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        columns = reader.fieldnames
        rows = list(reader)
        groups = {x: [] for x in columns}
        for column in columns:
            for row in rows:
                if row[column] != '':
                    groups[column].append(row[column])
        for key, value in groups.items():
            groupMax = value[0]
            groupRanks = value[1:]
            groups[key] = (groupMax, groupRanks)

    with open('Fight Night Rankings - Test Auditionee Rankings.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        columns = reader.fieldnames
        rows = list(reader)
        auditionees = {x: [] for x in columns}
        for column in columns:
            for row in rows:
                if row[column] != '':
                    auditionees[column].append(row[column])
    return groups, auditionees

def main():
    groups, auditionees = test_csv()
    groupList = []
    auditioneeList = []
    for groupname,groupinfo in groups.items():
        groupList.append(Group(groupname, groupinfo[1], int(groupinfo[0])))
    for auditioneename,ranking in auditionees.items():
        auditioneeList.append(Auditionee(auditioneename, ranking))
    # auditioneematcher(groupList, auditioneeList)
    # print('Auditionee Matching:')
    # for group in groupList:
    #     aveRank = 0
    #     for auditionee in group.newMembers:
    #         aveRank += group.rankings.index(auditionee.name) + 1
    #     aveRank /= len(group.newMembers)
    #     print(f'New members for {group.name} (ave rank: {aveRank}):')
    #     for member in group.newMembers:
    #         print(f'{member.name}, group ranking: {group.rankings.index(member.name) + 1}')
    #     print()
    # for group in groupList:
    #     group.newMembers = []
    # for auditionee in auditioneeList:
    #     auditionee.group = None

    print("=====================================================")
    groupmatcher(groupList, auditioneeList)
    print('Group Matching:')
    for group in groupList:
        aveRank = 0
        for auditionee in group.newMembers:
            aveRank += group.rankings.index(auditionee.name) + 1
        aveRank /= len(group.newMembers)
        print(f'New members for {group.name} (ave rank: {aveRank}):')
        for member in group.newMembers:
            print(f'{member.name}, group ranking: {group.rankings.index(member.name) + 1}')
        print()
    for auditionee in auditioneeList:
        if auditionee.group == None:
            print(f'{auditionee.name} was not matched')
        # else:
        #     print(f'{auditionee.name} was matched with {auditionee.group.name}')
main()
        