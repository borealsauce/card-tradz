import json,random
random.seed(42)
users=[
 ("you","You (Demo)","Carlsbad, CA",4.9,37,0,"2h"),
 ("slabking_mike","Mike R.","Phoenix, AZ",4.9,212,1,"20m"),
 ("graded_gems","Tasha W.","Charlotte, NC",4.8,148,2,"1h"),
 ("pc_hunter22","Jordan L.","Columbus, OH",4.7,63,3,"3h"),
 ("hobbybox_dan","Dan K.","Tampa, FL",4.95,401,0,"15m"),
 ("rookie_vault","Priya S.","Seattle, WA",4.6,41,5,"6h"),
 ("chrome_chaser","Luis M.","San Antonio, TX",4.85,97,1,"45m"),
 ("vintage_vic","Victor H.","Pittsburgh, PA",5.0,320,0,"1h"),
 ("pokepulls_amy","Amy T.","Portland, OR",4.75,88,2,"2h"),
 ("goatcards","Chris B.","Brooklyn, NY",4.4,29,7,"12h"),
 ("dimecollects","Nate G.","Denver, CO",4.8,156,1,"30m"),
 ("sundaysubs","Keisha J.","Atlanta, GA",4.9,119,0,"1h"),
]
U=[dict(handle=h,name=n,loc=l,rating=r,trades=t,cancels=c,resp=rs,joined=random.choice(["2021","2022","2023","2024"])) for h,n,l,r,t,c,rs in users]
cards=[
("Basketball","LeBron James","2003 Topps Chrome","#111 Rookie",950),
("Basketball","Luka Doncic","2018 Panini Prizm","#280 Rookie",420),
("Basketball","Victor Wembanyama","2023 Panini Prizm","#136 Rookie",310),
("Basketball","Stephen Curry","2009 Topps","#321 Rookie",640),
("Basketball","Giannis Antetokounmpo","2013 Panini Prizm","#290 Rookie",780),
("Basketball","Anthony Edwards","2020 Panini Prizm","#258 Rookie",260),
("Basketball","Michael Jordan","1997 Upper Deck","#18",180),
("Basketball","Caitlin Clark","2024 Panini Prizm WNBA","#22 Rookie",290),
("Basketball","Kobe Bryant","1996 Topps Chrome","#138 Rookie",1650),
("Basketball","Nikola Jokic","2015 Panini Prizm","#?? Rookie",350),
("Football","Patrick Mahomes","2017 Panini Prizm","#269 Rookie",720),
("Football","Josh Allen","2018 Panini Prizm","#205 Rookie",380),
("Football","Justin Jefferson","2020 Panini Prizm","#398 Rookie",210),
("Football","C.J. Stroud","2023 Panini Prizm","#339 Rookie",160),
("Football","Tom Brady","2000 Bowman","#236 Rookie",1400),
("Football","Joe Burrow","2020 Panini Prizm","#307 Rookie",240),
("Football","Jayden Daniels","2024 Panini Prizm","#331 Rookie",190),
("Football","Lamar Jackson","2018 Panini Prizm","#212 Rookie",230),
("Baseball","Shohei Ohtani","2018 Topps Update","#US1 Rookie",520),
("Baseball","Mike Trout","2011 Topps Update","#US175 Rookie",880),
("Baseball","Juan Soto","2018 Topps Update","#US300 Rookie",150),
("Baseball","Ken Griffey Jr.","1989 Upper Deck","#1 Rookie",620),
("Baseball","Elly De La Cruz","2023 Topps Chrome Update","#USC1 Rookie",140),
("Baseball","Paul Skenes","2024 Topps Chrome Update","#USC150 Rookie",210),
("Baseball","Derek Jeter","1993 SP","#279 Rookie",1100),
("Baseball","Aaron Judge","2017 Topps","#287 Rookie",240),
("Hockey","Connor McDavid","2015 Upper Deck Young Guns","#201 Rookie",1250),
("Hockey","Wayne Gretzky","1979 O-Pee-Chee","#18 Rookie",4800),
("Hockey","Connor Bedard","2023 Upper Deck Young Guns","#451 Rookie",420),
("Soccer","Lionel Messi","2014 Panini Prizm World Cup","#12",360),
("Soccer","Erling Haaland","2020 Topps Chrome UCL","#61 Rookie",280),
("Soccer","Kylian Mbappe","2018 Panini Prizm World Cup","#80 Rookie",330),
("Pokemon","Charizard","1999 Pokemon Base Set","#4 Holo",2600),
("Pokemon","Pikachu Illustrator Tribute","2023 Pokemon 151","#173 SIR",180),
("Pokemon","Umbreon VMAX","2021 Evolving Skies","#215 Alt Art",900),
("Pokemon","Lugia V","2022 Silver Tempest","#186 Alt Art",230),
]
for i,c in enumerate(cards):
    if "??" in c[3]: cards[i]=(c[0],c[1],c[2],"#291 Rookie",c[4])
graders=["PSA","PSA","PSA","BGS","SGC","CGC","CSG"]
def grade_for(g):
    if g=="BGS": return random.choice(["9","9.5","9.5","10"])
    if g in("CGC","CSG"): return random.choice(["9","9.5","10"])
    return random.choice(["8","9","9","10","10"])
mult={"8":0.35,"9":0.6,"9.5":0.85,"10":1.0}
import datetime
def mkcomps(fair,n=None):
    n=n or random.randint(5,8);out=[]
    for k in range(n):
        d=datetime.date(2026,10,17)-datetime.timedelta(days=random.randint(1,85))
        src=random.choice(["eBay sold","eBay sold","eBay sold","Alt"])
        typ=random.choice(["Auction","Buy It Now","Best Offer accepted"]) if src=="eBay sold" else random.choice(["Alt Marketplace","Alt Auction"])
        out.append(dict(date=d.isoformat(),source=src,type=typ,price=round(fair*random.uniform(.86,1.14))))
    return sorted(out,key=lambda c:c["date"],reverse=True)
L=[]
for i in range(60):
    sport,player,set_,num,base=cards[i%len(cards)] if i<len(cards) else random.choice(cards)
    g=random.choice(graders);gr=grade_for(g)
    if g=="BGS" and gr=="10": base*=1.6
    fair=round(base*mult[gr]*random.uniform(.85,1.15))
    comps=mkcomps(fair)
    ps=sorted(c["price"] for c in comps); fair=ps[len(ps)//2]
    r=random.random()
    price=round(fair*(random.uniform(.85,.97) if r<.3 else random.uniform(.97,1.06) if r<.75 else random.uniform(1.12,1.45)))
    owner=random.choice(U[1:])["handle"]
    mode=random.choice(["sale","trade","both","both"])
    variant=random.choice(["Base","Base","Base","Silver","Refractor","Holo","Gold /50","Red /299"]) if sport!="Pokemon" else "Holo"
    L.append(dict(id=f"L{1000+i}",sport=sport,player=player,set=set_,num=num,variant=variant,grader=g,grade=gr,
      cert=str(random.randint(10**7,10**8-1)) if g!="BGS" else "00"+str(random.randint(10**7,10**8-1)),
      pop=random.randint(3,4200),price=price,fair=fair,comps=comps,owner=owner,mode=mode,
      listed=f"2026-10-{random.randint(1,18):02d}",views=random.randint(20,2400),
      hue=random.randint(0,359)))
mine=[]
picks=[(0,"PSA","9",620,"2023-02-14"),(10,"PSA","10",410,"2022-08-03"),(18,"PSA","9",290,"2024-01-20"),(32,"PSA","8",900,"2021-11-05"),
 (26,"BGS","9.5",980,"2023-06-11"),(2,"PSA","10",380,"2024-07-02"),(13,"SGC","10",210,"2024-09-15"),(29,"PSA","10",300,"2022-12-01"),(34,"CGC","9.5",820,"2025-03-09")]
for j,(ci,g,gr,cost,pd) in enumerate(picks):
    sport,player,set_,num,base=cards[ci]
    fair=round(base*mult[gr]*random.uniform(.9,1.2)); comps=mkcomps(fair,7)
    ps=sorted(c["price"] for c in comps)
    mine.append(dict(id=f"M{j+1}",sport=sport,player=player,set=set_,num=num,variant="Base" if sport!="Pokemon" else "Holo",grader=g,grade=gr,
      cert=str(random.randint(10**7,10**8-1)),pop=random.randint(50,3000),fair=ps[len(ps)//2],comps=comps,owner="you",
      mode=random.choice(["none","trade","both"]),price=round(ps[len(ps)//2]*1.03),cost=cost,costDate=pd,hideCost=(j==3),hue=random.randint(0,359),listed="2026-10-01",views=random.randint(5,300)))
json.dump(dict(users=U,listings=L,mine=mine,catalog=[dict(sport=a,player=b,set=c,num=d,base=e) for a,b,c,d,e in cards]),open("data/listings.json","w"),indent=1)
print(len(L))
