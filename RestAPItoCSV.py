from xlwt import Workbook

import json, requests
from datetime import datetime
from datetime import timedelta
import traceback
import time

class a:

#SMF
    def getSmp(self, startDate, endDate):
        url = "https://api.epias.com.tr/epias/exchange/transparency/market/smp"

        querystring = {"startDate": startDate, "endDate": endDate}

        headers = {
            'Accept': "application/json",
            'X-IBM-Client-Id': "dcb02234-f6fb-4cf8-b904-29465c092a1b"
        }

        data = requests.request("GET", url, headers=headers, params=querystring)
        self.data = data.json()
        self.getname="getSmp"

    #PTF
    def getMcp(self,startDate, endDate):
        url = "https://api.epias.com.tr/epias/exchange/transparency/market/day-ahead-mcp"

        querystring = {"startDate": startDate.strftime("%Y-%m-%d"), "endDate": endDate.strftime("%Y-%m-%d")}

        headers = {
            'Accept': "application/json",
            'X-IBM-Client-Id': "dcb02234-f6fb-4cf8-b904-29465c092a1b"
        }
        data = requests.request("GET", url, headers=headers, params=querystring)
        self.data = data.json()
        self.getname = "getMcp"

    def getAOF(self,startDate, endDate):
        url = "https://api.epias.com.tr/epias/exchange/transparency/market/intra-day-summary"

        querystring = {"startDate": startDate.strftime("%Y-%m-%d"), "endDate": endDate.strftime("%Y-%m-%d")}

        headers = {
            'X-IBM-Client-Id': "dcb02234-f6fb-4cf8-b904-29465c092a1b"
        }

        data = requests.request("GET", url, headers=headers, params=querystring)
        self.data = data.json()
        self.getname = "getAOF"

    def excell(self,data):


        data= data["body"]
        jsondumps=data.keys()
        headers=[
            []
        ]
        allLimit = []

        for i in jsondumps:

            for x in range(len(data[i])):

                dataKeys = data[i][x].keys()
                dataKeys= list(dataKeys)
                csvData = ["None"] * len(dataKeys) *2

                for z in range(len(dataKeys)):
                    dataIndex = 0
                    try:
                       dataIndex = headers[0].index(i +"_"+dataKeys[z])
                    except:
                        headers[0].append(i +"_"+dataKeys[z])
                    dataIndex = headers[0].index(i +"_"+dataKeys[z])

                    csvData[dataIndex] = data[i][x][dataKeys[z]]

                headers.append(csvData)
            allLimit.append(len(headers))


        wb = Workbook()
        sheet = wb.add_sheet('Sheet 1')

        limitRow = 0
        excelRow = 0
        for k in range(len(headers)):
            if k >= allLimit[limitRow]:
                excelRow = 1
                limitRow +=1
            for f in range(len(headers[k])):
                if headers[k][f] == "None":
                    continue
                #print(str(excelRow) + " - " + str(f) )
                sheet.write(excelRow, f, headers[k][f])
            excelRow += 1

        wb.save('CSV_'+self.getname+'.CSV')
        print("csv file saved.")

    def run(self):
        date = datetime.strptime(datetime.today().strftime("%Y-%m-%d 00:00:00"), "%Y-%m-%d 00:00:00")
        self.startDate = date - timedelta(days=1)
        self.endDate = date + timedelta(days=1)
        self.getSmp(self.startDate, self.endDate)
        self.excell(self.data)
        self.getMcp(self.startDate, self.endDate)
        self.excell(self.data)
        self.getAOF(self.startDate, self.endDate)
        self.excell(self.data)

if __name__ == '__main__':
    a().run()
