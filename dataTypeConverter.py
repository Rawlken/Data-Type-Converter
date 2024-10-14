print('''--------------------------------------------------------
Byte = B
KiloByte = KB
MegaByte = MB
GigaByte = GB
TerraByte = TB
PetaByte = PB
ExaByte = EB
ZettaByte = ZB
YottaByte = YB
BrontoByte = BB
GeopByte = GEB
--------------------------------------------------------''')
while True:
    data_type1 = input("Enter First Data Type: ")
    data = float(input("Enter Data Value: "))
    data_type2 = input("Enter Second Data Type: ")

    if(data_type1 == "B") and (data_type2 == "KB"):
        b_to_kb = data / 1024
        print(b_to_kb , "KB")
    elif(data_type1 == "B") and (data_type2 == "MB"):
        b_to_mb = data / 1048576
        print(b_to_mb , "MB")
    elif(data_type1 == "B") and (data_type2 == "GB"):
        b_to_gb = data / 1073741824
        print(b_to_gb , "GB")
    elif(data_type1 == "B") and (data_type2 == "TB"):
        b_to_tb = data / 1099511627776
        print(b_to_tb , "TB")
    elif(data_type1 == "B") and (data_type2 == "PB"):
        b_to_pb = data / 1125899906842624
        print(b_to_pb , "PB")
    elif(data_type1 == "B") and (data_type2 == "EB"):
        b_to_eb = data / 1152921504606847e+18
        print(b_to_eb , "EB")
    elif(data_type1 == "B") and (data_type2 == "ZB"):
        b_to_zb = data / 1180591620717411e+36
        print(b_to_zb , "ZB")
    elif(data_type1 == "B") and (data_type2 == "YB"):
        b_to_yb = data / 1208925819614629e+39
        print(b_to_yb , "YB")
    elif(data_type1 == "B") and (data_type2 == "BB"):
        b_to_bb = data / 123794003928538e+42
        print(b_to_bb , "BB")
    elif(data_type1 == "B") and (data_type2 == "GEB"):
        b_to_geb = data / 1267650600228229e+45
        print(b_to_geb , "GEB")
    
    if(data_type1 == "KB") and (data_type2 == "B"):
        kb_to_b = data * 1024
        print(kb_to_b , "B")
    elif(data_type1 == "MB") and (data_type2 == "B"):
        mb_to_b = data * 1048576
        print(mb_to_b , "B")
    elif(data_type1 == "GB") and (data_type2 == "B"):
        gb_to_b = data * 1073741824
        print(gb_to_b , "B")
    elif(data_type1 == "TB") and (data_type2 == "B"):
        tb_to_b = data * 1099511627776
        print(tb_to_b , "B")
    elif(data_type1 == "PB") and (data_type2 == "B"):
        pb_to_b = data * 1125899906842624
        print(pb_to_b , "B")
    elif(data_type1 == "EB") and (data_type2 == "B"):
        eb_to_b = data * 1152921504606847e+18
        print(eb_to_b , "B")
    elif(data_type1 == "ZB") and (data_type2 == "B"):
        zb_to_b = data * 1180591620717411e+36
        print(zb_to_b , "B")
    elif(data_type1 == "YB") and (data_type2 == "B"):
        yb_to_b = data * 1208925819614629e+39
        print(yb_to_b , "B")
    elif(data_type1 == "BB") and (data_type2 == "B"):
        bb_to_b = data * 123794003928538e+42
        print(bb_to_b , "B")
    elif(data_type1 == "GEB") and (data_type2 == "B"):
        geb_to_b = data * 1267650600228229e+45
        print(geb_to_b , "B")
    
    if(data_type1 == "KB") and (data_type2 == "MB"):
        kb_to_mb = data / 1024
        print(kb_to_mb , "MB")
    elif(data_type1 == "KB") and (data_type2 == "GB"):
        kb_to_gb = data / 1048576
        print(kb_to_gb , "GB")
    elif(data_type1 == "KB") and (data_type2 == "TB"):
        kb_to_tb = data / 1073741824
        print(kb_to_tb , "TB")
    elif(data_type1 == "KB") and (data_type2 == "PB"):
        kb_to_pb = data / 10995116e+12
        print(kb_to_pb , "PB")
    elif(data_type1 == "KB") and (data_type2 == "EB"):
        kb_to_eb = data / 11258999e+15
        print(kb_to_eb , "EB")
    elif(data_type1 == "KB") and (data_type2 == "ZB"):
        kb_to_zb = data / 11529215e+18
        print(kb_to_zb , "ZB")
    elif(data_type1 == "KB") and (data_type2 == "YB"):
        kb_to_yb = data / 11805916e+21
        print(kb_to_yb , "YB")
    elif(data_type1 == "KB") and (data_type2 == "BB"):
        kb_to_bb = data / 12089258e+24
        print(kb_to_bb , "BB")
    elif(data_type1 == "KB") and (data_type2 == "GEB"):
        kb_to_geb = data / 1.23794e+27
        print(kb_to_geb , "GEB")
    
    if(data_type1 == "MB") and (data_type2 == "KB"):
        mb_to_kb = data * 1024
        print(mb_to_kb , "KB")
    elif(data_type1 == "GB") and (data_type2 == "KB"):
        gb_to_kb = data * 1048576
        print(gb_to_kb , "KB")
    elif(data_type1 == "TB") and (data_type2 == "KB"):
        tb_to_kb = data * 1073741824
        print(tb_to_kb , "KB")
    elif(data_type1 == "PB") and (data_type2 == "KB"):
        pb_to_kb = data * 10995116e+12
        print(pb_to_kb , "KB")
    elif(data_type1 == "EB") and (data_type2 == "KB"):
        eb_to_kb = data * 11258999e+15
        print(eb_to_kb , "KB")
    elif(data_type1 == "ZB") and (data_type2 == "KB"):
        zb_to_kb = data * 11529215e+18
        print(zb_to_kb , "KB")
    elif(data_type1 == "YB") and (data_type2 == "KB"):
        yb_to_kb = data * 11805916e+21
        print(yb_to_kb , "KB")
    elif(data_type1 == "BB") and (data_type2 == "KB"):
        bb_to_kb = data * 12089258e+24
        print(bb_to_kb , "KB")
    elif(data_type1 == "GEB") and (data_type2 == "KB"):
        geb_to_kb = data * 123794e+27
        print(geb_to_kb , "KB")
    
    if(data_type1 == "MB") and (data_type2 == "GB"):
        mb_to_gb = data / 1024
        print(mb_to_gb , "GB")
    elif(data_type1 == "MB") and (data_type2 == "TB"):
        mb_to_tb = data / 1048576
        print(mb_to_tb , "TB")
    elif(data_type1 == "MB") and (data_type2 == "PB"):
        mb_to_pb = data / 1073741824
        print(mb_to_pb , "PB")
    elif(data_type1 == "MB") and (data_type2 == "EB"):
        mb_to_eb = data / 10995116e+12
        print(mb_to_eb , "EB")
    elif(data_type1 == "MB") and (data_type2 == "ZB"):
        mb_to_zb = data / 11258999e+15
        print(mb_to_zb , "ZB")
    elif(data_type1 == "MB") and (data_type2 == "YB"):
        mb_to_yb = data / 11529215e+18
        print(mb_to_yb , "YB")
    elif(data_type1 == "MB") and (data_type2 == "BB"):
        mb_to_bb = data / 11805916e+21
        print(mb_to_bb , "BB")
    elif(data_type1 == "MB") and (data_type2 == "GEB"):
        mb_to_geb = data / 12089258e+24
        print(mb_to_geb , "GEB")
    
    if(data_type1 == "GB") and (data_type2 == "MB"):
        gb_to_mb = data * 1024
        print(gb_to_mb , "MB")
    elif(data_type1 == "TB") and (data_type2 == "MB"):
        tb_to_mb = data * 1048576
        print(tb_to_mb , "MB")
    elif(data_type1 == "PB") and (data_type2 == "MB"):
        pb_to_mb = data * 1073741824
        print(pb_to_mb , "MB")
    elif(data_type1 == "EB") and (data_type2 == "MB"):
        eb_to_mb = data * 10995116e+12
        print(eb_to_mb , "MB")
    elif(data_type1 == "ZB") and (data_type2 == "MB"):
        zb_to_mb = data * 11258999e+15
        print(zb_to_mb , "MB")
    elif(data_type1 == "YB") and (data_type2 == "MB"):
        yb_to_mb = data * 11529215e+18
        print(yb_to_mb , "MB")
    elif(data_type1 == "BB") and (data_type2 == "MB"):
        bb_to_mb = data * 11805916e+21
        print(bb_to_mb , "MB")
    elif(data_type1 == "GEB") and (data_type2 == "MB"):
        geb_to_mb = data * 12089258e+24
        print(geb_to_mb , "MB")
    
    if(data_type1 == "GB") and (data_type2 == "TB"):
        gb_to_tb = data / 1024
        print(gb_to_tb , "TB")
    elif(data_type1 == "GB") and (data_type2 == "PB"):
        gb_to_pb = data / 1048576
        print(gb_to_pb , "PB")
    elif(data_type1 == "GB") and (data_type2 == "EB"):
        gb_to_eb = data / 1073741824
        print(gb_to_eb , "EB")
    elif(data_type1 == "GB") and (data_type2 == "ZB"):
        gb_to_zb = data / 10995116e+12
        print(gb_to_zb , "ZB")
    elif(data_type1 == "GB") and (data_type2 == "YB"):
        gb_to_yb = data / 11258999e+15
        print(gb_to_yb , "YB")
    elif(data_type1 == "GB") and (data_type2 == "BB"):
        gb_to_bb = data / 11529215e+18
        print(gb_to_bb , "BB")
    elif(data_type1 == "GB") and (data_type2 == "GEB"):
        gb_to_geb = data / 11805916e+21
        print(gb_to_geb , "GEB")
    
    if(data_type1 == "TB") and (data_type2 == "GB"):
        tb_to_gb = data * 1024
        print(tb_to_gb , "GB")
    elif(data_type1 == "PB") and (data_type2 == "GB"):
        pb_to_gb = data * 1048576
        print(pb_to_gb , "GB")
    elif(data_type1 == "EB") and (data_type2 == "GB"):
        eb_to_gb = data * 1073741824
        print(eb_to_gb , "GB")
    elif(data_type1 == "ZB") and (data_type2 == "GB"):
        zb_to_gb = data * 10995116e+12
        print(zb_to_gb , "GB")
    elif(data_type1 == "YB") and (data_type2 == "GB"):
        yb_to_gb = data * 11258999e+15
        print(yb_to_gb , "GB")
    elif(data_type1 == "BB") and (data_type2 == "GB"):
        bb_to_gb = data * 11529215e+18
        print(bb_to_gb , "GB")
    elif(data_type1 == "GEB") and (data_type2 == "GB"):
        geb_to_gb = data * 11805916e+21
        print(geb_to_gb , "GB")
    
    if(data_type1 == "TB") and (data_type2 == "PB"):
        tb_to_pb = data / 1024
        print(tb_to_pb , "PB")
    elif(data_type1 == "TB") and (data_type2 == "EB"):
        tb_to_eb = data / 1048576
        print(tb_to_eb , "EB")
    elif(data_type1 == "TB") and (data_type2 == "ZB"):
        tb_to_zb = data / 1073741824
        print(tb_to_zb , "ZB")
    elif(data_type1 == "TB") and (data_type2 == "YB"):
        tb_to_yb = data / 10995116e+12
        print(tb_to_yb , "YB")
    elif(data_type1 == "TB") and (data_type2 == "BB"):
        tb_to_bb = data / 11258999e+15
        print(tb_to_bb , "BB")
    elif(data_type1 == "TB") and (data_type2 == "GEB"):
        tb_to_geb = data / 11529215e+18
        print(tb_to_geb , "GEB")
    
    if(data_type1 == "PB") and (data_type2 == "TB"):
        pb_to_tb = data * 1024
        print(pb_to_tb , "TB")
    elif(data_type1 == "EB") and (data_type2 == "TB"):
        eb_to_tb = data * 1048576
        print(eb_to_tb , "TB")
    elif(data_type1 == "ZB") and (data_type2 == "TB"):
        zb_to_tb = data * 1073741824
        print(zb_to_tb , "TB")
    elif(data_type1 == "YB") and (data_type2 == "TB"):
        yb_to_tb = data * 10995116e+12
        print(yb_to_tb , "TB")
    elif(data_type1 == "BB") and (data_type2 == "TB"):
        bb_to_tb = data * 11258999e+15
        print(bb_to_tb , "TB")
    elif(data_type1 == "GEB") and (data_type2 == "TB"):
        geb_to_tb = data * 11529215e+18
        print(geb_to_tb , "TB")
    
    if(data_type1 == "PB") and (data_type2 == "EB"):
        pb_to_eb = data / 1024
        print(pb_to_eb , "EB")
    elif(data_type1 == "PB") and (data_type2 == "ZB"):
        pb_to_zb = data / 1048576
        print(pb_to_zb , "ZB")
    elif(data_type1 == "PB") and (data_type2 == "YB"):
        pb_to_yb = data / 1073741824
        print(pb_to_yb , "YB")
    elif(data_type1 == "PB") and (data_type2 == "BB"):
        pb_to_bb = data / 10995116e+12
        print(pb_to_bb , "BB")
    elif(data_type1 == "PB") and (data_type2 == "GEB"):
        pb_to_geb = data / 11258999e+15
        print(pb_to_geb , "GEB")
    
    if(data_type1 == "EB") and (data_type2 == "PB"):
        eb_to_pb = data * 1024
        print(eb_to_pb , "PB")
    elif(data_type1 == "ZB") and (data_type2 == "PB"):
        zb_to_pb = data * 1048576
        print(zb_to_pb , "PB")
    elif(data_type1 == "YB") and (data_type2 == "PB"):
        yb_to_pb = data * 1073741824
        print(yb_to_pb , "PB")
    elif(data_type1 == "BB") and (data_type2 == "PB"):
        bb_to_pb = data * 10995116e+12
        print(bb_to_pb , "PB")
    elif(data_type1 == "GEB") and (data_type2 == "PB"):
        geb_to_pb = data * 11258999e+15
        print(geb_to_pb , "PB")
    
    if(data_type1 == "EB") and (data_type2 == "ZB"):
        eb_to_zb = data / 1024
        print(eb_to_zb , "ZB")
    elif(data_type1 == "EB") and (data_type2 == "YB"):
        eb_to_yb = data / 1048576
        print(eb_to_yb , "YB")
    elif(data_type1 == "EB") and (data_type2 == "BB"):
        eb_to_bb = data / 1073741824
        print(eb_to_bb , "BB")
    elif(data_type1 == "EB") and (data_type2 == "GEB"):
        eb_to_geb = data / 10995116e+12
        print(eb_to_geb , "GEB")
    
    if(data_type1 == "ZB") and (data_type2 == "EB"):
        zb_to_eb = data * 1024
        print(zb_to_eb , "EB")
    elif(data_type1 == "YB") and (data_type2 == "EB"):
        yb_to_eb = data * 1048576
        print(yb_to_eb , "EB")
    elif(data_type1 == "BB") and (data_type2 == "EB"):
        bb_to_eb = data * 1073741824
        print(bb_to_eb , "EB")
    elif(data_type1 == "GEB") and (data_type2 == "EB"):
        geb_to_eb = data * 10995116e+12
        print(geb_to_eb , "EB")
    
    if(data_type1 == "ZB") and (data_type2 == "YB"):
        zb_to_yb = data / 1024
        print(zb_to_yb , "YB")
    elif(data_type1 == "ZB") and (data_type2 == "BB"):
        zb_to_bb = data / 1048576
        print(zb_to_bb , "BB")
    elif(data_type1 == "ZB") and (data_type2 == "GEB"):
        zb_to_geb = data / 1073741824
        print(zb_to_geb , "GEB")
    
    if(data_type1 == "YB") and (data_type2 == "ZB"):
        yb_to_zb = data * 1024
        print(yb_to_zb , "ZB")
    elif(data_type1 == "BB") and (data_type2 == "ZB"):
        bb_to_zb = data * 1048576
        print(bb_to_zb , "ZB")
    elif(data_type1 == "GEB") and (data_type2 == "ZB"):
        geb_to_zb = data * 1073741824
        print(geb_to_zb , "ZB")
    
    if(data_type1 == "YB") and (data_type2 == "BB"):
        yb_to_bb = data / 1024
        print(yb_to_bb , "BB")
    elif(data_type1 == "YB") and (data_type2 == "GEB"):
        yb_to_geb = data / 1048576
        print(yb_to_geb , "GEB")
    
    if(data_type1 == "BB") and (data_type2 == "YB"):
        bb_to_yb = data * 1024
        print(bb_to_yb , "YB")
    elif(data_type1 == "GEB") and (data_type2 == "YB"):
        geb_to_yb = data * 1048576
        print(geb_to_yb , "YB")
    
    if(data_type1 == "BB") and (data_type2 == "GEB"):
        bb_to_geb = data / 1024
        print(bb_to_geb , "GEB")
    
    if(data_type1 == "GEB") and (data_type2 == "BB"):
        geb_to_bb = data * 1048576
        print(geb_to_bb , "BB")
