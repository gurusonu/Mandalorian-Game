import random
import time
from bgimpx import Pxl
from man import Man
from input import *
class Board:
	def __init__(self,pixel_values,mtr,manx,many):
		self._pixel_values=pixel_values
		self._counter=0
		self._life=100
		self._sleep_time=0.0002
		self._elife=3
		self._mtr=mtr
		self._ebullet_pos=[]
		self._nbullet_pos=[]
		self._manx=manx
		self._many=many
		self._ec=0
		self._grid = [[' ' for i in range(2400)] for j in range(50)]
		self._bullet_pos=[]
		self._old_bullet_pos=[]
		self._bullet_len=[]
		self._boss_enemy=[['B' for i in range(10)] for j in range(10)]
		self._last_many=38
	def Binit(self):
		# for x in range(0,50):
		# 	for y in range(0,238):
		# 		self._grid[x][y]="\x1b[38;2;"+str(self.gr_pixel_values[x][y][0])+";"+str(self._pixel_values[x][y][1])+";"+str(self._pixel_values[x][y][2])+"m\u2588\x1b[0m"
		# return self._grid
		for x in range(0,238):
			self._grid[0][x]="#"
			self._grid[1][x]="#"
			self._grid[47][x]="_"
			self._grid[48][x]="#"
			self._grid[49][x]="#"
		for x in range(238,238*2):
			self._grid[0][x]="@"
			self._grid[1][x]="@"
			self._grid[47][x]="_"
			self._grid[48][x]="@"
			self._grid[49][x]="@"
		for x in range(238*2,238*3):
			self._grid[0][x]="$"
			self._grid[1][x]="$"
			self._grid[47][x]="_"
			self._grid[48][x]="$"
			self._grid[49][x]="$"
		for x in range(238*3,238*4):
			self._grid[0][x]="?"
			self._grid[1][x]="?"
			self._grid[47][x]="_"
			self._grid[48][x]="?"
			self._grid[49][x]="?"
		for x in range(238*4,2400):
			self._grid[0][x]="+"
			self._grid[1][x]="+"
			self._grid[47][x]="_"
			self._grid[48][x]="+"
			self._grid[49][x]="+"
		return self._grid
	def increase_count(self):
		self._counter+=1
		# return self._counter
	def get_px(self,sy,sx):
		return self._grid[sy][sx]
	def stick_life(self):
		l=random.randrange(20,31)
		x=1
		while x<=l:
			sx=random.randrange(4,1700)
			sy=random.randrange(2,46)
			if self._grid[sy][sx]==" ":
				self._grid[sy][sx]="❤️"
				x+=1
	def obstacles(self):
		l=random.randrange(30,51)
		x=1
		while x<=l:
			type_choice=random.randrange(1,5)
			if type_choice==1:
				o_len=random.randrange(3,26)
				sx=random.randrange(4,2000-o_len)
				sy=random.randrange(2,46)
				# flag=0
				for tt in range(o_len):
					if self._grid[sy][sx+tt]==" ":
						self._grid[sy][sx+tt]="\u2580"
			elif type_choice==2:
				o_len=random.randrange(2,15)
				sx=random.randrange(4,2000-26)
				sy=random.randrange(2,46-o_len)
				# flag=0
				for tt in range(o_len):
					if self._grid[sy+tt][sx]==" ":
						self._grid[sy+tt][sx]="\u2588"
			elif type_choice==3:
				o_len=random.randrange(3,14)
				sx=random.randrange(4,2000-o_len)
				sy=random.randrange(2,46-o_len)
				# print("OK")
				for xx in range(o_len):
					for yy in range(o_len):
						if xx==yy and self._grid[sy+xx][sx+yy]==" ":
							self._grid[sy+xx][sx+yy]="\u2580"
			elif type_choice==4:
				o_len=random.randrange(3,14)
				sx=random.randrange(4,2000-o_len)
				sy=random.randrange(2,46-o_len)
				# print("OK")
				for xx in range(o_len):
					for yy in range(o_len):
						if xx==yy and self._grid[sy+xx][sx+o_len-1-yy]==" ":
							self._grid[sy+xx][sx+o_len-1-yy]="\u2580"
	# print("")
			x+=1
	def rider_bullet_attack(self,y,z):
		oj=self.get_px(y,z)
		if oj==">":
			self._grid[y][z]=" "
			self._elife-=1
	def add_enemy_bullets(self):
		if self._ec%6==0:
			epos1=[self._last_many+4,2000+222]
			epos2=[self._last_many+6,2000+222]
			self._ebullet_pos.append(epos1)
			self._ebullet_pos.append(epos2)
		self._ec+=1
		
	def stick_enemy_bullets(self):
		i=0
		for x in self._ebullet_pos:
			if(x[1]>1900):
				self._grid[x[0]][x[1]+2]=" "
				self._grid[x[0]][x[1]]="<"
			else:
				self._grid[x[0]][x[1]]=" "
			self._ebullet_pos[i][1]-=2
			i+=1
	def add_bullets(self,x):
		pos=[self._many+1,self._manx+5+x]
		self._bullet_pos.append(pos)
		self._bullet_len.append(0)
	def nadd_bullets(self,x):
		# add_bullets(self,x):
		npos=[self._many+1,self._manx+4+x]
		self._nbullet_pos.append(npos)
	def stick_rider_bullets(self):
		i=0
		for x in self._nbullet_pos:
			if x[1]<2300:
				print(x[1])
				self._grid[x[0]][x[1]-2]=" "
				self._grid[x[0]][x[1]]=">"
			# else:	
				# self._grid[x[0]][x[1]]=" "
			self._nbullet_pos[i][1]+=2
			i+=1

		
	def process_bullets(self):
		i=0
		for x in self._bullet_pos:
			# print(x[1])
			if(x[1]==2300):
				self._grid[x[0]][x[1]]=" "
			if((x[1])<2300):
				# print(x[1])				
				self._grid[x[0]][x[1]-2]=" "
				rtc=self._grid[x[0]][x[1]]
				rtc1=self._grid[x[0]][x[1]-1]
				if(rtc=="\u2588"):
					u=x[0]-1
					t=x[0]
					while self._grid[t][x[1]]=="\u2588":
						self._grid[t][x[1]]=" "
						t+=1
					while self._grid[u][x[1]]=="\u2588":
						self._grid[u][x[1]]=" "
						u-=1
					self._grid[x[0]][x[1]]=" "
					self._bullet_len[i]=460
				elif(rtc1=="\u2588"):
					u=x[0]-1
					t=x[0]
					while self._grid[t][x[1]-1]=="\u2588":
						self._grid[t][x[1]-1]=" "
						t+=1
					while self._grid[u][x[1]-1]=="\u2588":
						self._grid[u][x[1]-1]=" "
						u-=1
					self._grid[x[0]][x[1]]=" "
					self._bullet_len[i]=460
				elif rtc=="\u2580":
					if self._grid[x[0]][x[1]+1]=="\u2580":
						u=x[1]-1
						t=x[1]
						while self._grid[x[0]][t]=="\u2580":
							self._grid[x[0]][t]=" "
							t+=1
						while self._grid[x[0]][u]=="\u2580":
							self._grid[x[0]][u]=" "
							u-=1
						self._grid[x[0]][x[1]]=" "
						self._bullet_len[i]=460
					elif self._grid[x[0]+1][x[1]+1]=="\u2580" or self._grid[x[0]-1][x[1]-1]=="\u2580":
						u1=x[1]-1
						u0=x[0]-1
						t0=x[0]
						t1=x[1]
						while self._grid[t0][t1]=="\u2580":
							self._grid[t0][t1]=" "
							t1+=1
							t0+=1
						while self._grid[u0][u1]=="\u2580":
							self._grid[u0][u1]=" "
							u0-=1
							u1-=1
						self._grid[x[0]][x[1]]=" "
						self._bullet_len[i]=460
					elif self._grid[x[0]+1][x[1]-1]=="\u2580" or self._grid[x[0]-1][x[1]+1]=="\u2580":
						u1=x[1]+1
						u0=x[0]-1
						t0=x[0]
						t1=x[1]
						while self._grid[t0][t1]=="\u2580":
							self._grid[t0][t1]=" "
							t0+=1
							t1-=1
						while self._grid[u0][u1]=="\u2580":
							self._grid[u0][u1]=" "
							u0-=1
							u1+=1
						self._grid[x[0]][x[1]]=" "
						self._bullet_len[i]=460
				elif rtc1=="\u2580":
					if self._grid[x[0]][x[1]]=="\u2580":
						u=x[1]-2
						t=x[1]-1
						while self._grid[x[0]][t]=="\u2580":
							self._grid[x[0]][t]=" "
							t+=1
						while self._grid[x[0]][u]=="\u2580":
							self._grid[x[0]][u]=" "
							u-=1
						self._grid[x[0]][x[1]]=" "
						self._bullet_len[i]=460
					elif self._grid[x[0]+1][x[1]]=="\u2580":
						u1=x[1]-2
						u0=x[0]-1
						t0=x[0]
						t1=x[1]-1
						while self._grid[t0][t1]=="\u2580":
							self._grid[t0][t1]=" "
							t1+=1
							t0+=1
						while self._grid[u0][u1]=="\u2580":
							self._grid[u0][u1]=" "
							u0-=1
							u1-=1
						self._grid[x[0]][x[1]]=" "
						self._bullet_len[i]=460
					elif self._grid[x[0]+1][x[1]-2]=="\u2580" or self._grid[x[0]-1][x[1]]=="\u2580":
						u1=x[1]
						u0=x[0]-1
						t0=x[0]
						t1=x[1]-1
						while self._grid[t0][t1]=="\u2580":
							self._grid[t0][t1]=" "
							t0+=1
							t1-=1
						while self._grid[u0][u1]=="\u2580":
							self._grid[u0][u1]=" "
							u0-=1
							u1+=1
						self._grid[x[0]][x[1]]=" "
						self._bullet_len[i]=460

				else:
					if(self._bullet_len[i]<460):
						self._grid[x[0]][x[1]]=">"
						self._bullet_pos[i][1]+=2
						self._bullet_len[i]+=2
				i+=1



	def increase_life(self):
		self._life+=1
	def get_life(self,y,z):
		oj=self.get_px(y,z)
		if(oj=="❤️"):
			self._grid[y][z]=" "
			self.increase_life()
	def coins(self):
		l=random.randrange(100,201)
		for x in range(l):
			o_len=random.randrange(1,11)
			sx=random.randrange(4,2000-26)
			sy=random.randrange(2,46)
			for tt in range(o_len):
				if self._grid[sy][sx+tt]==" ":
					self._grid[sy][sx+tt]="O"
	def coin_collision(self,y,z):
		oj=self.get_px(y,z)
		if(oj=="O"):
			self._grid[y][z]=" "
			self.increase_count()
	def beam_collision(self,y,z):
		oj=self.get_px(y,z)
		if(oj=="\u2580" or oj=="\u2588"):
			self._many=45
			self._life-=1
	def is_alive(self):
		if self._life==0:
			self._life=3
			return 0
		else:
			return 1
	def printBoard(self,x):
		# for x in range(1):
		for y in range(3):
			pr="\033["+str(self._many+y+1)+";"+str(self._manx+1)+"f"
			print(pr,end="")
			for z in range(3):
				print(self._mtr[y][z],end="")
			print("")
			# print("AA",end="")
		print("\033[0;0f",end="")
		for y in range(50):
			for z in range(x,238+x):
				if(y>=self._many and y<(self._many+3) and (z-x)>=self._manx and (z-x)<(self._manx+3)):
					self.coin_collision(y,z)
					self.beam_collision(y,z)
					self.get_life(y,z)
					print("\033[1C",end="")
				else:
					print(self._grid[y][z],end="")
			print("")
		# self.delete_bullets(manx,x)
		print("\033[51;0f",end="")
		for zz in range(238):
			print(" ",end="")
		print("")
		# print("\033[52;0f",end="")
		print("COUNT : ",self._counter)
		print("❤️ : ",self._life)
		time.sleep(0.0002)
	def enemyfight(self):
		for y in range(3):
			pr="\033["+str(self._many+y+1)+";"+str(self._manx+1)+"f"
			print(pr,end="")
			for z in range(3):
				print(self._mtr[y][z],end="")
			print("")
		print("\033[0;0f",end="")
		for y in range(10):
			pr="\033["+str(self._last_many+y+1)+";"+str(226)+"f"
			print(pr,end="")
			for z in range(10):
				print(self._boss_enemy[y][z],end="")
			print("")
		print("\033[0;0f",end="")
		for y in range(50):
			for z in range(2000,2238):
				if(y>=self._many and y<(self._many+3) and (z-2000)>=self._manx and (z-2000)<(self._manx+3)):
					print("\033[1C",end="")
				elif (y>=self._last_many and y<(self._last_many+10) and (z-2000)>=225 and(z-2000)<235):
					self.rider_bullet_attack(y,z)
					print("\033[1C",end="")
				else:
					print(self._grid[y][z],end="")
			print("")
		print("\033[51;0f",end="")
		for zz in range(238):
			print(" ",end="")
		print("")
		# print("\033[52;0f",end="")
		print("COUNT : ",self._counter)
		print("❤️ : ",self._life)
		print(self._elife)
		time.sleep(0.0002)


# if __name__=="__main__":
	def move_right(self):
		if self._manx<=233:
			self._manx+=2
	def move_up(self):
		if self._many>=4:
			self._last_many=self._many-6
			self._many-=2
			if self._last_many<2:
				self._last_many=2
		elif self._many<4:
			self._many=2
			self._last_many=self._many
	def move_left(self):
		if self._manx>=2:
			self._manx-=2
	def gravity(self):
		if self._many<45:
			self._last_many=self._many-6
			self._many+=1
			if self._last_many<2:
				self._last_many=2
obj1=Pxl("dawn.jpg")
pixel_values=obj1.getpx()
obj2=Man()
mtr=obj2.getman()
obj3=Board(pixel_values,mtr,3,45)
grid=obj3.Binit()
obj3.obstacles()
obj3.coins()
obj3.stick_life()
# manx=3
# many=45

# thread1=threading.Thread(target=printBoard,daemon=True,args=)
flag=0
flag1=0

if(flag==0 and flag1==0):
	while True:
		obj3.enemyfight()
		obja1=Get()
		chbuff=input_to(obja1)
		obj3.add_enemy_bullets()
		obj3.stick_enemy_bullets()
		ckk=obj3.is_alive()
		if(ckk==0):
			print("Game Over")
			# flag=1
			break
		# obj3.printBoard(x)
		if chbuff != 'e':
			if chbuff=='d':
				# manx+=2
				obj3.move_right()
			elif chbuff=='w':
				# many-=2
				obj3.move_up()
			elif chbuff=='w':
				# many=2
				obj3.move_up()
			elif chbuff=='a':
				# manx-=2
				obj3.move_left()
			elif chbuff=='s':
				obj3.nadd_bullets(2000)
				# print(x)
			if chbuff !='w':
				# many+=1
				obj3.gravity()
			obj3.stick_rider_bullets()
			# obj3.delete_bullets()
			# print(obj3._bullet_pos)
		else:
			print("\033[54;0f",end="")
			break

