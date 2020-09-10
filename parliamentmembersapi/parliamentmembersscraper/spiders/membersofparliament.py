import scrapy
import html
import re
import urllib.parse
from datetime import datetime
from parliamentmembersscraper.items import ParliamentmembersscraperItem
from .schemavalidator import PrimeMinisterSchema
from pydantic import ValidationError

class ParliamentMemberSpider(scrapy.Spider):
    name = 'parliamentmembers'
    start_urls = ['https://www.parliament.bg/bg/MP']
    def parse(self, response):

        for member in response.xpath("//div[@class = 'MPinfo']/a/@href").getall():
            info_page = urllib.parse.urljoin('https://www.parliament.bg/export.php/bg/xml/MP/',
                                             str([int(s) for s in member.split('/') if s.isdigit()][0]))
            yield scrapy.Request(info_page, callback=self.parse_more_info)

    def parse_more_info(self, response):
        item = ParliamentmembersscraperItem()

        if response.xpath(u"//DateOfBirth[@value]").get() is not None:
            to_be_stripped_date_of_birth = html.unescape(response.xpath(u"//DateOfBirth[@value]").get())
            stripped_date_of_birth = re.findall(r'"([^"]*)"', to_be_stripped_date_of_birth)
            item['date_of_birth'] = datetime.strptime(stripped_date_of_birth[0], '%d/%m/%Y').date()
        else:
            print("No DoB parsed")
            item['date_of_birth'] = None

        if response.xpath(u"//FirstName[@value]").get() is not None:
            to_be_stripped_first_name = html.unescape(response.xpath(u"//FirstName[@value]").get())
            stripped_first_name = re.findall(r'"([^"]*)"', to_be_stripped_first_name)
            item['first_name'] = stripped_first_name[0]
        else:
            print("No FN parsed")
            item['first_name'] = None

        if response.xpath(u"//FamilyName[@value]").get() is not None:
            to_be_stripped_last_name = html.unescape(response.xpath(u"//FamilyName[@value]").get())
            stripped_last_name = re.findall(r'"([^"]*)"', to_be_stripped_last_name)
            item['last_name'] = stripped_last_name[0]
        else:
            print("No LN parsed")
            item['last_name'] = None

        if response.xpath(u"//PlaceOfBirth[@value]").get() is not None:
            to_be_stripped_place_of_birth = html.unescape(response.xpath(u"//PlaceOfBirth[@value]").get())
            stripped_place_of_birth = re.findall(r'"([^"]*)"', to_be_stripped_place_of_birth)
            item['place_of_birth'] = stripped_place_of_birth[0]
        else:
            print("No PoB parsed")
            item['place_of_birth'] = None

        if response.xpath(u"//PoliticalForce[@value]").get() is not None:
            to_be_stripped_political_force = html.unescape(response.xpath(u"//PoliticalForce[@value]").get())
            stripped_political_force = re.findall(r'"([^"]*)"', to_be_stripped_political_force)
            stripped_political_force[0] = stripped_political_force[0].split(' ')
            pp = ['ГЕРБ', 'БСП', 'ДПС', 'ОБЕДИНЕНИ', 'ВОЛЯ']
            for i in stripped_political_force[0]:
                if i not in pp:
                    pass
                elif i == 'ОБЕДИНЕНИ':
                    item['political_force'] = 'ОП'
                else:
                    item['political_force'] = i
        else:
            print("No PF parsed")
            item['political_force'] = None

        if response.xpath(u"//Language[@value]").get() is not None:
            to_be_stripped_language = html.unescape(response.xpath(u"//Language[@value]").getall())
            stripped = []
            for element in to_be_stripped_language:
                languages = re.findall(r'"([^"]*)"', html.unescape(element))
                for language in languages:
                    if language.isdigit():
                        pass
                    else:
                        stripped.append(language)
            try:
                item['language1'] = stripped[0]
            except:
                item['language1'] = None
            try:
                item['language2'] = stripped[1]
            except:
                item['language2'] = None
            try:
                item['language3'] = stripped[2]
            except:
                item['language3'] = None
            try:
                item['language4'] = stripped[3]
            except:
                item['language4'] = None
            try:
                item['language5'] = stripped[4]
            except:
                item['language5'] = None
        else:
            print("No Language parsed")
            item['language1'] = None
            item['language2'] = None
            item['language3'] = None
            item['language4'] = None
            item['language5'] = None

        if response.xpath(u"//E-mail[@value]").get() is not None:
            to_be_stripped_email = html.unescape(response.xpath(u"//E-mail[@value]").get())
            stripped_email = re.findall(r'"([^"]*)"', to_be_stripped_email)
            if not stripped_email[0]:
                item['email'] = None
            else:
                print(stripped_email[0])
                item['email'] = stripped_email[0]
        else:
            print("No email parsed")
            item['email'] = None

        if response.xpath(u"//Profession[@value]").get() is not None:

            to_be_stripped_profession = html.unescape(response.xpath(u"//Profession[@value]").getall())
            stripped = []
            for element in to_be_stripped_profession:
                professions = re.findall(r'"([^"]*)"', html.unescape(element))
                for profession in professions:
                    if profession.isdigit():
                        pass
                    else:
                        stripped.append(profession)
            try:
                item['profession1'] = stripped[0]
            except:
                item['profession1'] = None
            try:
                item['profession2'] = stripped[1]
            except:
                item['profession2'] = None
        else:
            print("No profession parsed")
            item['profession1'] = None
            item['profession2'] = None
        try:
            PrimeMinisterSchema(first_name=item['first_name'], last_name=item['last_name'], date_of_birth=item['date_of_birth'],
                                place_of_birth=item['place_of_birth'], political_force=item['political_force'],
                                language1=item['language1'],language2=item['language2'],language3=item['language3'],
                                language4=item['language4'],language5=item['language5'], email=item['email'],
                                profession1=item['profession1'],profession2=item['profession2'])
            return item
        except ValidationError as e:
            print(e.json())
            print("validation failed")