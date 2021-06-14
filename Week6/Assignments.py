'''
import random

num = []
for i in range(10000):
    num.append(random.randint(1,10))

d = {1:0 , 2:0 , 3:0 , 4:0 , 5:0, 6:0 , 7:0 , 8:0 , 9:0 , 10:0}

for i in num:
    d[i] += 1

def check(d, n):
    s = 0
    for i in d:
        s += d[i]
    return s == n

print(check(d, len(num)))

t1 = (1,2,3)
#t2 = (10)
t3 = 20,
t4 = tuple([10])
#t5 = tuple((10))
t6 = 1, 2, 3

print(type(t1), type(t3), type(t4), type(t6))

#s1 = {}
s2 = set([1])
s3 = {1}
s4 = set()
#s5 = set((1))
#s6 = set(1)

print(type(s2), type(s3), type(s4))

records = {
    1:{
        'name':'ram',
        'age':18,
        'school':'kv',
        'marks':{'p':100, 'm':100, 'c':100}
    },
    2:{
        'name':'sham',
        'age':19,
        'school':'kv',
        'marks':{'p':100, 'm':100, 'c':100}
    }
}

print (records)

records.update({3:{'name': 'lax', 'age': 18, 'school': 'kv', 'marks': {'p': 100, 'm': 100, 'c': 100}}})
records.pop(2)


print(records)
'''

'''
myWords = ['It.', 'was', 'Monday', 'morning.', 'Swaminathan', 'was', 'reluctant', 'to', 'open', 'his',
 'eyes.', 'He', 'considered', 'Monday', 'specially', 'unpleasant', 'in', 'the', 'calendar.', 'After',
 'the', 'delicious', 'freedom', 'of', 'Saturday', 'And', 'Sunday,', 'it', 'was', 'difficult', 'to',
 'get', 'into', 'the', 'Monday', 'mood', 'of', 'work', 'and', 'discipline.', 'He', 'shuddered', 'at',
 'the', 'very', 'thought', 'of', 'school:', 'the', 'dismal', 'yellow', 'building;', 'the',
 'fire-eyed', 'Vedanayagam,', 'his', 'class', 'teacher,', 'and', 'headmaster', 'with', 'his',
 'thin', 'long', 'cane...']

def freqWords(words):
    processedWords = []
    for word in words:
        word = word.lower()
        if (not word.isalpha()):
            word = word.strip(',')
            word = word.strip(';')
            word = word.strip(':')
            word = word.strip('.')
            word = word.strip('!')
        processedWords.append(word)
    
    d = {}

    if(len(words) == 0):
        return d
    
    for word in processedWords:
        count = processedWords.count(word)
        if (count in d.keys()):
            if (word not in d[count]):
                d[count].append(word)
        else:
            d[count] = [word]
    
    return d

print(freqWords(myWords))
'''

'''
scores = [
    { 'Chemistry': 78,
    'CityTown': 'Erode',
    'DateOfBirth': '7 Nov',
    'Gender': 'M',
    'Mathematics': 68,
    'Name': 'Bhuvanesh',
    'Physics': 64,
    'SeqNo': 0,
    'Total': 210},
    
    { 'Chemistry': 91,
        'CityTown': 'Salem',
        'DateOfBirth': '3 Jun',
        'Gender': 'M',
        'Mathematics': 62,
        'Name': 'Harish',
        'Physics': 45,
        'SeqNo': 1,
        'Total': 198},
    
    { 'Chemistry': 77,
        'CityTown': 'Chennai',
        'DateOfBirth': '4 Jan',
        'Gender': 'M',
        'Mathematics': 57,
        'Name': 'Shashank',
        'Physics': 54,
        'SeqNo': 2,
        'Total': 188},
    
    { 'Chemistry': 78,
        'CityTown': 'Chennai',
        'DateOfBirth': '5 May',
        'Gender': 'F',
        'Mathematics': 42,
        'Name': 'Rida',
        'Physics': 53,
        'SeqNo': 3,
        'Total': 173},
    
    { 'Chemistry': 89,
        'CityTown': 'Madurai',
        'DateOfBirth': '17 Nov',
        'Gender': 'F',
        'Mathematics': 87,
        'Name': 'Ritika',
        'Physics': 64,
        'SeqNo': 4,
        'Total': 240},
    
    { 'Chemistry': 84,
        'CityTown': 'Chennai',
        'DateOfBirth': '8 Feb',
        'Gender': 'F',
        'Mathematics': 71,
        'Name': 'Akshaya',
        'Physics': 92,
        'SeqNo': 5,
        'Total': 247},
    
    { 'Chemistry': 87,
        'CityTown': 'Ambur',
        'DateOfBirth': '23 Mar',
        'Gender': 'M',
        'Mathematics': 81,
        'Name': 'Sameer',
        'Physics': 82,
        'SeqNo': 6,
        'Total': 250},
    
    { 'Chemistry': 76,
        'CityTown': 'Vellore',
        'DateOfBirth': '15 Mar',
        'Gender': 'M',
        'Mathematics': 84,
        'Name': 'Aditya',
        'Physics': 92,
        'SeqNo': 7,
        'Total': 252},
    
    { 'Chemistry': 51,
        'CityTown': 'Bengaluru',
        'DateOfBirth': '28 Feb',
        'Gender': 'M',
        'Mathematics': 74,
        'Name': 'Surya',
        'Physics': 64,
        'SeqNo': 8,
        'Total': 189},
    
    { 'Chemistry': 73,
        'CityTown': 'Bengaluru',
        'DateOfBirth': '6 Dec',
        'Gender': 'M',
        'Mathematics': 63,
        'Name': 'Clarence',
        'Physics': 88,
        'SeqNo': 9,
        'Total': 224},
    
    { 'Chemistry': 68,
        'CityTown': 'Chennai',
        'DateOfBirth': '12 Jan',
        'Gender': 'F',
        'Mathematics': 64,
        'Name': 'Kavya',
        'Physics': 72,
        'SeqNo': 10,
        'Total': 204},
    
    { 'Chemistry': 92,
        'CityTown': 'Bengaluru',
        'DateOfBirth': '30 Apr',
        'Gender': 'M',
        'Mathematics': 97,
        'Name': 'Rahul',
        'Physics': 92,
        'SeqNo': 11,
        'Total': 281},
    
    { 'Chemistry': 71,
        'CityTown': 'Chennai',
        'DateOfBirth': '14 Jan',
        'Gender': 'F',
        'Mathematics': 52,
        'Name': 'Srinidhi',
        'Physics': 64,
        'SeqNo': 12,
        'Total': 187},
    
    { 'Chemistry': 89,
        'CityTown': 'Madurai',
        'DateOfBirth': '6 May',
        'Gender': 'M',
        'Mathematics': 65,
        'Name': 'Gopi',
        'Physics': 73,
        'SeqNo': 13,
        'Total': 227},
    
    { 'Chemistry': 93,
        'CityTown': 'Trichy',
        'DateOfBirth': '23 July',
        'Gender': 'F',
        'Mathematics': 89,
        'Name': 'Sophia',
        'Physics': 62,
        'SeqNo': 14,
        'Total': 244},
    
    { 'Chemistry': 90,
        'CityTown': 'Theni',
        'DateOfBirth': '22 Sep',
        'Gender': 'F',
        'Mathematics': 76,
        'Name': 'Goutami',
        'Physics': 58,
        'SeqNo': 15,
        'Total': 224},
    
    { 'Chemistry': 43,
        'CityTown': 'Trichy',
        'DateOfBirth': '30 Dec',
        'Gender': 'M',
        'Mathematics': 87,
        'Name': 'Tauseef',
        'Physics': 86,
        'SeqNo': 16,
        'Total': 216},
    
    { 'Chemistry': 67,
        'CityTown': 'Chennai',
        'DateOfBirth': '14 Dec',
        'Gender': 'M',
        'Mathematics': 62,
        'Name': 'Arshad',
        'Physics': 81,
        'SeqNo': 17,
        'Total': 210},
    
    { 'Chemistry': 97,
        'CityTown': 'Erode',
        'DateOfBirth': '9 Oct',
        'Gender': 'F',
        'Mathematics': 72,
        'Name': 'Abirami',
        'Physics': 92,
        'SeqNo': 18,
        'Total': 261},
    
    { 'Chemistry': 62,
        'CityTown': 'Trichy',
        'DateOfBirth': '30 Aug',
        'Gender': 'M',
        'Mathematics': 56,
        'Name': 'Vetrivel',
        'Physics': 78,
        'SeqNo': 19,
        'Total': 196},
    
    { 'Chemistry': 91,
        'CityTown': 'Vellore',
        'DateOfBirth': '17 Sep',
        'Gender': 'M',
        'Mathematics': 93,
        'Name': 'Kalyan',
        'Physics': 68,
        'SeqNo': 20,
        'Total': 252},
    
    { 'Chemistry': 74,
        'CityTown': 'Bengaluru',
        'DateOfBirth': '15 Mar',
        'Gender': 'F',
        'Mathematics': 78,
        'Name': 'Monika',
        'Physics': 69,
        'SeqNo': 21,
        'Total': 221},
    
    { 'Chemistry': 57,
        'CityTown': 'Nagercoil',
        'DateOfBirth': '17 Jul',
        'Gender': 'F',
        'Mathematics': 62,
        'Name': 'Priya',
        'Physics': 62,
        'SeqNo': 22,
        'Total': 181},
    
    { 'Chemistry': 88,
        'CityTown': 'Bengaluru',
        'DateOfBirth': '13 May',
        'Gender': 'F',
        'Mathematics': 97,
        'Name': 'Deepika',
        'Physics': 91,
        'SeqNo': 23,
        'Total': 276},
    
    { 'Chemistry': 58,
        'CityTown': 'Madurai',
        'DateOfBirth': '26 Dec',
        'Gender': 'M',
        'Mathematics': 44,
        'Name': 'Siddharth',
        'Physics': 72,
        'SeqNo': 24,
        'Total': 174},
    
    { 'Chemistry': 92,
        'CityTown': 'Chennai',
        'DateOfBirth': '16 May',
        'Gender': 'F',
        'Mathematics': 87,
        'Name': 'Geeta',
        'Physics': 75,
        'SeqNo': 25,
        'Total': 254},
    
    { 'Chemistry': 82,
        'CityTown': 'Chennai',
        'DateOfBirth': '22 Jul',
        'Gender': 'M',
        'Mathematics': 74,
        'Name': 'JK',
        'Physics': 71,
        'SeqNo': 26,
        'Total': 227},
    
    { 'Chemistry': 52,
        'CityTown': 'Madurai',
        'DateOfBirth': '4 Mar',
        'Gender': 'M',
        'Mathematics': 81,
        'Name': 'Jagan',
        'Physics': 76,
        'SeqNo': 27,
        'Total': 209},
    
    { 'Chemistry': 83,
        'CityTown': 'Madurai',
        'DateOfBirth': '10 Sep',
        'Gender': 'F',
        'Mathematics': 74,
        'Name': 'Nisha',
        'Physics': 83,
        'SeqNo': 28,
        'Total': 240},
    
    { 'Chemistry': 81,
        'CityTown': 'Vellore',
        'DateOfBirth': '13 Oct',
        'Gender': 'M',
        'Mathematics': 72,
        'Name': 'Naveen',
        'Physics': 66,
        'SeqNo': 29,
        'Total': 219}]
'''

'''
def crowdedGroup(scores, subject, markLimit):
    subject = subject.title()
    subjectMarksOfStudents = []
    minSubMarks = 100
    maxSubMarks = 0
    for i in scores:
        temp = []
        temp.append(i[subject])
        temp.append(i['SeqNo'])
        subjectMarksOfStudents.append(temp)
        if (minSubMarks > i[subject]):
            minSubMarks = i[subject]
        if (maxSubMarks < i[subject]):
            maxSubMarks = i[subject]
    
    d = {}
    for i in range(minSubMarks, maxSubMarks+1):
        minMarksForBin = i
        maxMarksForBin = i + markLimit
        if (maxMarksForBin < maxSubMarks):
            key = (minMarksForBin, maxMarksForBin)
            d[key] = []
        else:
            key = (minMarksForBin, maxSubMarks)
            d[key] = []
            break

    for i in subjectMarksOfStudents:
        studentSubMarks = i[0]
        studentSeqNo = i[1]
        for j in d.keys():
            minForGroup = j[0]
            maxForGroup = j[1]
            if (studentSubMarks <= maxForGroup and studentSubMarks >= minForGroup):
                d[j].append(studentSeqNo)
    
    maxGroupCount = 0
    for i in d.keys():
        if (maxGroupCount < len(d[i])):
            maxGroupCount = len(d[i])
    
    outputList = []
    for i in d.keys():
        if (maxGroupCount == len(d[i]) and d[i] not in outputList):
            outputList.append(d[i])

    return outputList

    for i in outputSet:
        for j in i:
            print(j, end=" ")
        print("")

crowdedGroup(scores, 'physics', 25)
'''

'''
def topMentors(scores, subject):
    subject = subject.title()

    d = {}
    for mentor in scores:
        mentorSeqNo = mentor['SeqNo']
        mentorSubMarks = mentor[subject]
        d[mentorSeqNo] = []
        menteeMinMarks = mentorSubMarks - 20
        menteeMaxMarks = mentorSubMarks - 10
        
        for mentee in scores:
            menteeSubMarks = mentee[subject]
            if (menteeSubMarks <= menteeMaxMarks and menteeSubMarks >= menteeMinMarks):
                d[mentorSeqNo].append(mentee['SeqNo'])
    
    maxMenteeCount = 0
    for i in d.keys():
        if (maxMenteeCount < len(d[i])):
            maxMenteeCount = len(d[i])
    
    outputDict = {}
    for i in d.keys():
        if (maxMenteeCount == len(d[i])):
            outputDict[i] = d[i]
    
    return outputDict
    
print(topMentors(scores, 'physics'))
'''