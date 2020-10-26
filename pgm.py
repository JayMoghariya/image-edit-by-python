# name: File path of the pgm image file
# Output is a 2D list of integers
import math
def readpgm(name):
	image = []
	with open(name) as f:
		lines = list(f.readlines())
		if len(lines) < 3:
			print("Wrong Image Format\n")
			exit(0)

		count = 0
		width = 0
		height = 0
		for line in lines:
			if line[0] == '#':
				continue

			if count == 0:
				if line.strip() != 'P2':
					print("Wrong Image Type\n")
					exit(0)
				count += 1
				continue

			if count == 1:
				dimensions = line.strip().split(' ')
				print(dimensions)
				width = dimensions[0]
				height = dimensions[1]
				count += 1
				continue

			if count == 2:	
				allowable_max = int(line.strip())
				if allowable_max != 255:
					print("Wrong max allowable value in the image\n")
					exit(0)
				count += 1
				continue

			data = line.strip().split()
			data = [int(d) for d in data]
			image.append(data)
	return image	
def avarageimage(image):
    h=len(image)
    image1=[]
    for k in range(len(image)):
        image1.append(image[k][:])
    w=len(image[0])
    for i in range(h):
        for j in range(w):
            if (i!=0 and j!=0 and i!=h-1 and j!=w-1):
                image1[i][j]=int((image[i-1][j-1]+image[i-1][j]+image[i-1][j+1]+image[i][j-1]+image[i][j]+image[i][j+1]+image[i+1][j-1]+ image[i+1][j]+image[i+1][j+1])/9)
    return image1
# img is the 2D list of integers
# file is the output file path
def edgedetection(image):
    h=len(image)
    image1=[]
    for k in range(len(image)):
        image1.append(image[k][:])
    #or image1=[[0 for i in range(w)]for k in range(h)]
    w=len(image[0])
    gg=4*(math.sqrt(2))
    for i in range(h):
        for j in range(w):
            if (i!=0 and j!=0 and i!=h-1 and j!=w-1):
                hdif = (image[i-1][j-1]-image[i-1][j+1]) + 2*(image[i][j-1]-image[i][j+1]) + (image[i+1][j-1]-image[i+1][j+1])
                vdif = (image[i-1][j-1]-image[i+1][j-1]) + 2*(image[i-1][j]-image[i+1][j]) + (image[i-1][j+1]-image[i+1][j+1])
                image1[i][j] = int((math.sqrt(hdif*hdif + vdif*vdif))/gg)
            elif (i==0 and j==0):
                hdif= image[1][1]+(2*image[0][1])
                vdif=image[1][1]+(2*image[1][0])          
                image1[0][0]=int((math.sqrt(hdif*hdif + vdif*vdif))/gg)
            elif (i==0 and j==w-1):
                 hdif= image[1][w-2]+(2*image[0][w-2])
                 vdif=image[1][w-2]+(2*image[1][w-1])
                 image1[0][w-1]=int((math.sqrt(hdif*hdif + vdif*vdif))/gg)
            elif (i==h-1 and j==0):
                hdif= image[h-2][1]+(2*image[h-1][1])
                vdif=image[h-2][1]+(2*image[h-2][0])
                image1[h-1][0]=int((math.sqrt(hdif*hdif + vdif*vdif))/gg)
            elif (i==h-1 and j==w-1):
                hdif= image[h-2][w-2]+(2*image[h-1][w-2])
                vdif=image[h-2][w-2]+(2*image[h-2][w-2])
                image1[h-1][w-1]=int((math.sqrt(hdif*hdif + vdif*vdif))/gg)
            elif (i==0 and j!=0 and j!=w-1):
                hdif = 2*(image[i][j-1]-image[i][j+1]) + (image[i+1][j-1]-image[i+1][j+1])
                vdif = 2*(image[i-1][j]-image[i+1][j]) + (image[i-1][j+1]-image[i+1][j+1])
                image1[i][j] = int((math.sqrt(hdif*hdif + vdif*vdif))/gg)
            elif (i==h-1 and j!=0 and j!=w-1):
                hdif = (image[i-1][j-1]-image[i-1][j+1]) + 2*(image[i][j-1]-image[i][j+1])
                vdif = (image[i-1][j-1]) + 2*(image[i-1][j])+(image[i-1][j+1])
                image1[i][j] = int((math.sqrt(hdif*hdif + vdif*vdif))/gg)
            elif (j==0 and i!=0 and i!=h-1):
                hdif = (image[i-1][j+1]) + 2*(image[i][j+1]) + (image[i+1][j+1])
                vdif = 2*(image[i-1][j]-image[i+1][j]) + (image[i-1][j+1]-image[i+1][j+1])
                image1[i][j] = int((math.sqrt(hdif*hdif + vdif*vdif))/gg)
            elif (j==w-1 and i!=0 and i!=h-1):
                hdif = (image[i-1][j-1]) + 2*(image[i][j-1]) + (image[i+1][j-1])
                vdif = (image[i-1][j-1]-image[i+1][j-1]) + 2*(image[i-1][j]-image[i+1][j])
                image1[i][j] = int((math.sqrt(hdif*hdif + vdif*vdif))/gg)
    return image1
def Minenergy(image,image1):
    w=len(image[0])
    h=len(image)
    minenergy=[[[0]for i in range(w)]for j in range(h)]
    #t=[[minenergy[0][i]]for i in range(h)]
    for j in range(h):
        for i in range(w):
            if (i!=0 and i!=w-1 and j!=0):
                aa=min(minenergy[j-1][i-1][0], minenergy[j-1][i][0], minenergy[j-1][i+1][0])
                minenergy[j][i][0]= image[j][i] + aa
                if aa==minenergy[j-1][i-1][0]:
                    minenergy[j][i].append(i-1)
                if aa==minenergy[j-1][i][0]:
                    minenergy[j][i].append(i)
                if aa==minenergy[j-1][i+1][0]:
                    minenergy[j][i].append(i+1)
                #q=minenergy[i-1].index(aa)
                #t.append([i-1][q])
            elif i==0 and j!=0:
                bb=min(minenergy[j-1][i][0], minenergy[j-1][i+1][0])
                minenergy[j][i][0]= image[j][i] + bb
                if bb==minenergy[j-1][i][0]:
                    minenergy[j][i].append(i)
                if bb==minenergy[j-1][i+1]:
                    minenergy[j][i].append(i+1)
                #hh=minenergy[i-1].index(bb)
                #t.append([i-1][hh])
            elif i==w-1 and j!=0:
                cc=min(minenergy[j-1][i-1][0], minenergy[j-1][i][0])
                minenergy[j][i][0]= image[j][i] + cc
                if cc==minenergy[j-1][i-1]:
                    minenergy[j][i].append(i-1)
                if cc==minenergy[j-1][i]:
                    minenergy[j][i].append(i)
                #v=minenergy[i-1].index(cc)
                #t.append([i-1][v])
            elif j==0:
                minenergy[j][i][0]=image[j][i]
    
    sss=[]
    def retracing(i,j,sss,minenergy):
        sss.append([i,j])
        if i!=0:
            for w in minenergy[i][j][1:]:
                retracing(i-1,w,sss,minenergy)
        return sss
    uu=minenergy[h-1]
    vv=list(zip(*uu))
    jj=min(vv[0])
    aaa=vv[0].count(jj)
    ee,temp=0,[]
    while ee<aaa:
        ee+=1
        vv=list(zip(*uu))
        bbb=vv[0].index(min(vv[0]))
        minenergy[h-1][bbb][0]=256*h
        temp+=retracing(h-1,bbb,sss,minenergy)
    for i in range(len(temp)):
        s=temp[i]
        image1[s[0]][s[1]]=255
    return image1
'''    def findminimum(l):
        i,j=l[0],l[1]
        if (i!=0 and i!=w-1 and j!=0):
            f=min(minenergy[i-1][j-1], minenergy[i-1][j], minenergy[i-1][j+1])
            if f==minenergy[i-1][j-1]:
                return [i-1,j-1]
            elif f==minenergy[i-1][j]:
                return [i-1,j]
            elif f==minenergy[i-1][j+1]:
                return [i-1,j+1]
        elif i==0 and j!=0:
            f=min(minenergy[i-1][j], minenergy[i-1][j+1])
            if f==minenergy[i-1][j]:
                return [i-1,j]
            elif f==minenergy[i-1][j+1]:
                return [i-1,j+1]
        elif i==w-1 and j!=0:
            f=min(minenergy[i-1][j-1], minenergy[i-1][j])
            if f==minenergy[i-1][j-1]:
                return [i-1,j-1]
            elif f==minenergy[i-1][j]:
                return [i-1,j]
        elif j==0:
            return None
    def removeminimum():
        b=min(minenergy[h-1])
        g=b.count(minenergy[h-1])
        t,c=0,[]
        while t<g:
            i=h-1
            j=minenergy[i].index(b)
            l=[i,j]
            c.append(l)
            while i>0 and j>=0:
                l=[i,j]
                ss=findminimum(l)
                c.append(ss)
                i-=1
                '''
                

def writepgm(img, file):
	with open(file, 'w') as fout:
		if len(img) == 0:
			pgmHeader = 'p2\n0 0\n255\n'
		else:
			pgmHeader = 'P2\n' + str(len(img[0])) + ' ' + str(len(img)) + '\n255\n'
			fout.write(pgmHeader)
			line = ''
			for i in img:
				for j in i:
					line += str(j) + ' '
			line += '\n'
			fout.write(line)


########## Function Calls ##########
x = readpgm('test.pgm')			# test.pgm is the image present in the same working directory
writepgm(x, 'test_o.pgm')		# x is the image to output and test_o.pgm is the image output in the same working directory
y=avarageimage(x)
writepgm(y,'average.pgm')
z=edgedetection(x)
writepgm(z,'edge.pgm')
writepgm(avarageimage(readpgm('flower_gray.pgm')),'outavg.pgm')
writepgm(edgedetection(readpgm('flower_gray.pgm')),'outedg.pgm')
writepgm(edgedetection(readpgm('mona_lisa.ascii.pgm')),'monaedge.pgm')
'''writepgm(avarageimage(readpgm('photo.pgm')),'extraavg.pgm')
writepgm(edgedetection(readpgm('photo.pgm')),'etraedg.pgm')
writepgm(Minenergy(z,x),'minenergy1.pgm')
writepgm(Minenergy(edgedetection(readpgm('flower_gray.pgm')),readpgm('flower_gray.pgm')),'minenergy2.pgm')'''
###################################
