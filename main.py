from channel import Channel
from sku import Sku
from vendor import Vendor


#Vendors
unca = Vendor("UNCA", "Jim Jones", "Brooklyn", "unca001","953 Eastern PKWY", "NY", "11213", "net60", "4321432", "1234123")
hyla = Vendor("HYLA","Johnny Cash","Doral","14628","28000 E Parkway Drive","FL","33178","net30","0025891","1152362")
sellnet = Vendor("SELLNET","Gisele Bundchen","Naples","2322","8954 One Way Place","FL","34101","net4","1022587","5637412")
pcs = Vendor("PCS","Janet Jackson","Toledo","back4512","7000 Pepper Court","OH","43615","allforyou","3268878","0035259")
sony = Vendor("SONY","Josephine Baker","Paris","002591x","1 Red Mill Place","TX","75462","net4","5208520","0031649")
tronix = Vendor("TRONIX","James Franco","Manhattan","as10525","4 Spider Cove","NY","10021","net15","1658974","2456987")
panda = Vendor("PANDA","Jim Walton","Springdale","500258","45 Comfy Lane","AR","72762","net3","6369854","6586258")
meem = Vendor("MEEM","Jeff Bezos","Seattle","riv525584","1000 Top Dog Avenue","WA","98104","net10","1001001","0010010")
raycon = Vendor("RAYCON","John F. Kennedy","Arlington","n456-3285","2400 1st Avenue","VA","76003","net60","5211258","6547412")
rico = Vendor("RICO","George W. Carver","Diamond","45606","8790 Pindar Way","MO","64840","net14","9852025","6369874")



#Skus
pau100 = Sku("PAU100","Apple","Iphone100","1 lb","6x2x1",300, "Used","Black",unca, 79.99, 109.99)
# pan200 = Sku("PAN200","Apple","Iphone200","1.2lb","6.5x2.5x0.15",500,"mia3","New","Red",unca,462,569.99)
# psn300 = Sku("PSN300","Samsung","Galaxy Alpha","1.3 lb","5.5x2.5x0.15",200,"mia3","New","Coral",sellnet,100,609.99)
# pnr400 = Sku("PNR400","Nokia","PhoneA","1 lb","6x2x0.10",500,"mia2","Refurbished","Blue",sellnet,70.54,198)
# psu500 = Sku("PSU500","Samsung","Fold","1.6 lb","7x3x0.2",50,"mia2","Used","Silver",sellnet,508,709.99)
# han600 = Sku("HAN600","Apple","Airpods","0.5lb","2.5x2.5x1",500,"mia4","New","White",hyla,50,109.99)
# han700 = Sku("HAN700","Apple","Airpods","0.5lb","2.5x2.5x1",500,"mia4","New","Black",hyla,55,119.99)
# hbu800 = Sku("HBU800","Beats","Beats1","2 lb","7.5x8.5x2.5",100,"mia4","Used","Red",sony,100,129.99)
# hbr900 = Sku("HBR900","Beats","Beats2","2 lb","7.5x8.5x2.5",90,"mia4","Refurbished","Red",sony,80,100.99)
# hsn1000 = Sku("HSN1000","Samsung","Pro","0.51 lb","2.5x1.2x0.5",200,"mia4","New","Lilac",pcs,40,99.99)
# hsn1100 = Sku("HSN1100","Samsung","Pro2","0.51 lb","2.5x1.2x0.5",200,"mia4","New","Black",pcs,40,99.99)
# sfn1200 = Sku("SFN1200","Faber-Castell","Watercolor","1lb","7.5x5.5x0.25",100,"mia5","New","Natural",tronix,8,17.99)
# sfn1300 = Sku("SFN1300","Faber-Castell","Truecolor","1lb","7.5x5.5x0.25",100,"mia5","New","Bright",tronix,8,17.99)
# szn1400 = Sku("SZN1400","Zebra","Midliners","1.2 lb","7.5x5.5x0.35",200,"mia5","New","Pastel",panda,9,29.99)
# szn1500 = Sku("SZN1500","Zebra","Highliners","1.2 lb","7.5x5.5x0.35",150,"mia5","New","Summer",panda,9,29.99)
# san1600 = Sku("SAN1600","Arteza","Paint Markers","2 lb","9.5x7x0.5",120,"mia5","New","Primary",meem,16.99,48.98)
# san1700 = Sku("SAN1700","Arteza","Water Markers","2 lb","9.5x7x0.5",140,"mia5","New","Greys",meem,18.99,56.98)
# fgn1800 = Sku("FGN1800","Guerlain","La Belle","1.4 lb","4.5x2.5x1",50,"mia6","New","Red",raycon,50,99.99)
# fcn1900 = Sku("FCN1900","Creed","Aventus","1.6 lb","5x2.4x1.1",60,"mia6","New","White",rico,104,205.99)
# ftn2000 = Sku("FTN2000","Tocca","Simone","1.2 lb","3.5x3.5x3.15",100,"mia6","New","Lilac",rico,40,89.99)



#Channels
amazon = Channel("Amazon", "Cam'ron","Marketplace", 5, 3.99, "30 Days", "90 Days", "Damon Dash")
wish = Channel("Wish","Dee'yon","Marketplace",4,4.99,"30 days","30 days","Dennis Rodman")
ebay = Channel("eBay","Kee'shon","Marketplace",5,5.99,"30 days","60 days","Dave Chappelle")
staples = Channel("Staples","Tray'von","Dropship",3,3.99,"60 days","120 days","Denzel Washington")
craigslist = Channel("Craigslist","Ann'twon","Dropship",5,6.99,"1 day","2 days","Diana Ross")


#Lists
# skus = [pau100, pan200, psn300, pnr400, psu500, han600, han700, hbu800, hbr900, hsn1000, hsn1100, sfn1200, sfn1300, szn1400, szn1500, san1600, san1700, fgn1800, fcn1900, ftn2000]

channels = [amazon, wish, ebay, staples, craigslist]

vendors = [unca, hyla, sellnet, pcs, sony, tronix, panda, meem, raycon, rico]


#Part 6:

'''avgcost = 1849.51/20
avgprce = 3456.789/20

total = 0
for s in skus:
  total = s.selling_price + total
  
print(total) ''' #used to verify totals and average price


# def avg_sku (skus):
#   total = 0
#   avg = 0
#   for _ in skus:
#     total = _.selling_price + total
#   avg = total/len(skus)
#   return avg

# print("The average SKU price is %.2f" %avg_sku(skus))


# #Part 7:

# def list_details(skus):
#   for _ in skus:
#     print(f"{_.part_number}:",_.manufacturer,_.model)

# list_details(skus)


# #Part 8:

# import random 

# def random_five(skus):
#   count = 0

#   for _ in skus:
#     if count < 5:
#       random_sku = random.choice(skus)
#       print(random_sku.part_number)
#       count += 1 

# random_five(skus)

#Swuzhere

print(pau100.warehouse_location)

pau100.add_stock("rma",10)