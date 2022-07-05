from abc import ABCMeta, abstractmethod


class Section(metaclass=ABCMeta): #팩토리 다이어그램(p480) : Product
    
    @abstractmethod
    def describe(self):
        pass


class PersonalSection(Section): # ConcreteProduct
    
    def describe(self):
        print("Personal Section")


class AlbumSection(Section):# ConcreteProduct
    
    def describe(self):
        print("Album Section")


class PatentSection(Section):# ConcreteProduct
    
    def describe(self):
        print("Patent Section")


class PublicationSection(Section):# ConcreteProduct
    
    def describe(self):
        print("Publication Section")


class Profile(metaclass=ABCMeta): #Creator
    
    def __init__(self):
        self.sections = []
        self.createProfile()
    
    @abstractmethod  # factory method (추상)
    def createProfile(self):
        pass
    
    def getSections(self):
        return self.sections
    
    def addSections(self, section):
        self.sections.append(section)


class linkedin(Profile): #팩토리 객체1, concreteCreator1
    
    def createProfile(self): #실제 팩토리 메소드 호출 , 팩토리 메소드 구상
        self.addSections(PersonalSection())
        self.addSections(PatentSection())
        self.addSections(PublicationSection())


class facebook(Profile): #팩토리 객체2 , concreteCreator2
    
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())
        #self.getSections(self)

# class twitter(Profile):
    
    # def createProfile(self):
    #     self.addSections(PatentSection())
    #     self.addSections(PublicationSection())
    

if __name__ == '__main__':
    
    profile_type = input("Which Profile you'd like to create? [LinkedIn or FaceBook]")
    profile = eval(profile_type.lower())()
    print("Creating Profile..", type(profile).__name__) #객체 이름 출력 코드(내부 메소드)
    print("Profile has sections --", profile.getSections())

    # for i in profile.sections:
    #     print(i.describe())