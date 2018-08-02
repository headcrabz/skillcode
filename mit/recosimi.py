
# coding: utf-8

# In[9]:


import numpy as np
import pandas as pd
import os
from hackathon.settings import BASE_DIR

# In[10]:
class getsimilarprofiles : 

	def getprofiles(self,profile, strength) :
		file_path = os.path.join(BASE_DIR, "mit/Skilllist3.xlsx")
		rd = pd.read_excel(file_path)


		rd=rd.fillna(0)


		rp = rd.pivot_table(columns=['Title'],index=['Skill'],values='Data Value')
		rp.head()

		##### insert Input occupation
		a = "Software Developers, Applications"
		if "application" in profile or "Application" in profile: 
			a= "Software Developers, Applications"
		elif "security" in profile :
			a="Information Security Analysts"
		else :
			a = profile

		
		boughta = rp[a]


		similara = rp.corrwith(boughta)
		similara = similara.dropna()
		df = pd.DataFrame(similara)


		k1=similara.sort_values(ascending=False).head(20)
		

		######## Can change similarity Coefficient Based on tuning. If high quality then high threshhold here
		k=k1[k1> strength]
		

		
		# for i,v in self.k.items():
		# 	# print similar jobs here (take as output in executable)
		#     print (i)

		return k


	def getrecommendedState(self,profile, strength):
		k = self.getprofiles(profile, strength)

		file_path = os.path.join(BASE_DIR, "mit/Location Wise Data.xlsx")
		location=pd.read_excel(file_path)
		s= pd.DataFrame(columns=list(location))


		for i,v in k.items():
		    t=location[location['Occupation title (click on the occupation title to view its profile)']==i]
		    s=s.append(t)

		d={}
		for a in s.State.unique():
			t=s[s['State']==a]
			d[a]=[t['Employment'].sum(),t['Total Jobs'].mean(), t['Annual mean wage'].mean() ]


		##### change minrequirement based on tuning parameter
		minrequirement = 10000
		m=500000
		for i in d.keys():
		    if d[i][0]>minrequirement:
		        if d[i][2]<m:
		            m=d[i][2]
		            p=i


		##### Output to print!!!!!!!

		result = {}
		
		result["Recommended State"] = p
		result["Average Annual wage"]  = str(d[p][2])
		result["Number of people in relevant job role"]  = str(d[p][0])
		result["Total number of working people"] = str(d[p][1])

		print result
		return (result , k)



# p = getsimilarprofiles()
# p.getprofiles("application", 0.8)

# p.getrecommendedState()

