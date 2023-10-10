print('''--------------------------------------------------------
This program made by Halil Buğra Bayraktar.
--------------------------------------------------------
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
    veri_tipi1 = input("Enter First Data Type: ")
    veri1 = float(input("Enter Data Value: "))
    veri_tipi2 = input("Enter Second Data Type: ")

    if(veri_tipi1 == "B") and (veri_tipi2 == "KB"):
        b_to_kb = veri1 / 1024
        print(b_to_kb , "KB")
    elif(veri_tipi1 == "B") and (veri_tipi2 == "MB"):
        b_to_mb = veri1 / 1048576
        print(b_to_mb , "MB")
    elif(veri_tipi1 == "B") and (veri_tipi2 == "GB"):
        b_to_gb = veri1 / 1073741824
        print(b_to_gb , "GB")
    elif(veri_tipi1 == "B") and (veri_tipi2 == "TB"):
        b_to_tb = veri1 / 1099511627776
        print(b_to_tb , "TB")
    elif(veri_tipi1 == "B") and (veri_tipi2 == "PB"):
        b_to_pb = veri1 / 1125899906842624
        print(b_to_pb , "PB")
    elif(veri_tipi1 == "B") and (veri_tipi2 == "EB"):
        b_to_eb = veri1 / 1152921504606847e+18
        print(b_to_eb , "EB")
    elif(veri_tipi1 == "B") and (veri_tipi2 == "ZB"):
        b_to_zb = veri1 / 1180591620717411e+36
        print(b_to_zb , "ZB")
    elif(veri_tipi1 == "B") and (veri_tipi2 == "YB"):
        b_to_yb = veri1 / 1208925819614629e+39
        print(b_to_yb , "YB")
    elif(veri_tipi1 == "B") and (veri_tipi2 == "BB"):
        b_to_bb = veri1 / 123794003928538e+42
        print(b_to_bb , "BB")
    elif(veri_tipi1 == "B") and (veri_tipi2 == "GEB"):
        b_to_geb = veri1 / 1267650600228229e+45
        print(b_to_geb , "GEB")
    
    if(veri_tipi1 == "KB") and (veri_tipi2 == "B"):
        kb_to_b = veri1 * 1024
        print(kb_to_b , "B")
    elif(veri_tipi1 == "MB") and (veri_tipi2 == "B"):
        mb_to_b = veri1 * 1048576
        print(mb_to_b , "B")
    elif(veri_tipi1 == "GB") and (veri_tipi2 == "B"):
        gb_to_b = veri1 * 1073741824
        print(gb_to_b , "B")
    elif(veri_tipi1 == "TB") and (veri_tipi2 == "B"):
        tb_to_b = veri1 * 1099511627776
        print(tb_to_b , "B")
    elif(veri_tipi1 == "PB") and (veri_tipi2 == "B"):
        pb_to_b = veri1 * 1125899906842624
        print(pb_to_b , "B")
    elif(veri_tipi1 == "EB") and (veri_tipi2 == "B"):
        eb_to_b = veri1 * 1152921504606847e+18
        print(eb_to_b , "B")
    elif(veri_tipi1 == "ZB") and (veri_tipi2 == "B"):
        zb_to_b = veri1 * 1180591620717411e+36
        print(zb_to_b , "B")
    elif(veri_tipi1 == "YB") and (veri_tipi2 == "B"):
        yb_to_b = veri1 * 1208925819614629e+39
        print(yb_to_b , "B")
    elif(veri_tipi1 == "BB") and (veri_tipi2 == "B"):
        bb_to_b = veri1 * 123794003928538e+42
        print(bb_to_b , "B")
    elif(veri_tipi1 == "GEB") and (veri_tipi2 == "B"):
        geb_to_b = veri1 * 1267650600228229e+45
        print(geb_to_b , "B")
    
    if(veri_tipi1 == "KB") and (veri_tipi2 == "MB"):
        kb_to_mb = veri1 / 1024
        print(kb_to_mb , "MB")
    elif(veri_tipi1 == "KB") and (veri_tipi2 == "GB"):
        kb_to_gb = veri1 / 1048576
        print(kb_to_gb , "GB")
    elif(veri_tipi1 == "KB") and (veri_tipi2 == "TB"):
        kb_to_tb = veri1 / 1073741824
        print(kb_to_tb , "TB")
    elif(veri_tipi1 == "KB") and (veri_tipi2 == "PB"):
        kb_to_pb = veri1 / 10995116e+12
        print(kb_to_pb , "PB")
    elif(veri_tipi1 == "KB") and (veri_tipi2 == "EB"):
        kb_to_eb = veri1 / 11258999e+15
        print(kb_to_eb , "EB")
    elif(veri_tipi1 == "KB") and (veri_tipi2 == "ZB"):
        kb_to_zb = veri1 / 11529215e+18
        print(kb_to_zb , "ZB")
    elif(veri_tipi1 == "KB") and (veri_tipi2 == "YB"):
        kb_to_yb = veri1 / 11805916e+21
        print(kb_to_yb , "YB")
    elif(veri_tipi1 == "KB") and (veri_tipi2 == "BB"):
        kb_to_bb = veri1 / 12089258e+24
        print(kb_to_bb , "BB")
    elif(veri_tipi1 == "KB") and (veri_tipi2 == "GEB"):
        kb_to_geb = veri1 / 1.23794e+27
        print(kb_to_geb , "GEB")
    
    if(veri_tipi1 == "MB") and (veri_tipi2 == "KB"):
        mb_to_kb = veri1 * 1024
        print(mb_to_kb , "KB")
    elif(veri_tipi1 == "GB") and (veri_tipi2 == "KB"):
        gb_to_kb = veri1 * 1048576
        print(gb_to_kb , "KB")
    elif(veri_tipi1 == "TB") and (veri_tipi2 == "KB"):
        tb_to_kb = veri1 * 1073741824
        print(tb_to_kb , "KB")
    elif(veri_tipi1 == "PB") and (veri_tipi2 == "KB"):
        pb_to_kb = veri1 * 10995116e+12
        print(pb_to_kb , "KB")
    elif(veri_tipi1 == "EB") and (veri_tipi2 == "KB"):
        eb_to_kb = veri1 * 11258999e+15
        print(eb_to_kb , "KB")
    elif(veri_tipi1 == "ZB") and (veri_tipi2 == "KB"):
        zb_to_kb = veri1 * 11529215e+18
        print(zb_to_kb , "KB")
    elif(veri_tipi1 == "YB") and (veri_tipi2 == "KB"):
        yb_to_kb = veri1 * 11805916e+21
        print(yb_to_kb , "KB")
    elif(veri_tipi1 == "BB") and (veri_tipi2 == "KB"):
        bb_to_kb = veri1 * 12089258e+24
        print(bb_to_kb , "KB")
    elif(veri_tipi1 == "GEB") and (veri_tipi2 == "KB"):
        geb_to_kb = veri1 * 123794e+27
        print(geb_to_kb , "KB")
    
    if(veri_tipi1 == "MB") and (veri_tipi2 == "GB"):
        mb_to_gb = veri1 / 1024
        print(mb_to_gb , "GB")
    elif(veri_tipi1 == "MB") and (veri_tipi2 == "TB"):
        mb_to_tb = veri1 / 1048576
        print(mb_to_tb , "TB")
    elif(veri_tipi1 == "MB") and (veri_tipi2 == "PB"):
        mb_to_pb = veri1 / 1073741824
        print(mb_to_pb , "PB")
    elif(veri_tipi1 == "MB") and (veri_tipi2 == "EB"):
        mb_to_eb = veri1 / 10995116e+12
        print(mb_to_eb , "EB")
    elif(veri_tipi1 == "MB") and (veri_tipi2 == "ZB"):
        mb_to_zb = veri1 / 11258999e+15
        print(mb_to_zb , "ZB")
    elif(veri_tipi1 == "MB") and (veri_tipi2 == "YB"):
        mb_to_yb = veri1 / 11529215e+18
        print(mb_to_yb , "YB")
    elif(veri_tipi1 == "MB") and (veri_tipi2 == "BB"):
        mb_to_bb = veri1 / 11805916e+21
        print(mb_to_bb , "BB")
    elif(veri_tipi1 == "MB") and (veri_tipi2 == "GEB"):
        mb_to_geb = veri1 / 12089258e+24
        print(mb_to_geb , "GEB")
    
    if(veri_tipi1 == "GB") and (veri_tipi2 == "MB"):
        gb_to_mb = veri1 * 1024
        print(gb_to_mb , "MB")
    elif(veri_tipi1 == "TB") and (veri_tipi2 == "MB"):
        tb_to_mb = veri1 * 1048576
        print(tb_to_mb , "MB")
    elif(veri_tipi1 == "PB") and (veri_tipi2 == "MB"):
        pb_to_mb = veri1 * 1073741824
        print(pb_to_mb , "MB")
    elif(veri_tipi1 == "EB") and (veri_tipi2 == "MB"):
        eb_to_mb = veri1 * 10995116e+12
        print(eb_to_mb , "MB")
    elif(veri_tipi1 == "ZB") and (veri_tipi2 == "MB"):
        zb_to_mb = veri1 * 11258999e+15
        print(zb_to_mb , "MB")
    elif(veri_tipi1 == "YB") and (veri_tipi2 == "MB"):
        yb_to_mb = veri1 * 11529215e+18
        print(yb_to_mb , "MB")
    elif(veri_tipi1 == "BB") and (veri_tipi2 == "MB"):
        bb_to_mb = veri1 * 11805916e+21
        print(bb_to_mb , "MB")
    elif(veri_tipi1 == "GEB") and (veri_tipi2 == "MB"):
        geb_to_mb = veri1 * 12089258e+24
        print(geb_to_mb , "MB")
    
    if(veri_tipi1 == "GB") and (veri_tipi2 == "TB"):
        gb_to_tb = veri1 / 1024
        print(gb_to_tb , "TB")
    elif(veri_tipi1 == "GB") and (veri_tipi2 == "PB"):
        gb_to_pb = veri1 / 1048576
        print(gb_to_pb , "PB")
    elif(veri_tipi1 == "GB") and (veri_tipi2 == "EB"):
        gb_to_eb = veri1 / 1073741824
        print(gb_to_eb , "EB")
    elif(veri_tipi1 == "GB") and (veri_tipi2 == "ZB"):
        gb_to_zb = veri1 / 10995116e+12
        print(gb_to_zb , "ZB")
    elif(veri_tipi1 == "GB") and (veri_tipi2 == "YB"):
        gb_to_yb = veri1 / 11258999e+15
        print(gb_to_yb , "YB")
    elif(veri_tipi1 == "GB") and (veri_tipi2 == "BB"):
        gb_to_bb = veri1 / 11529215e+18
        print(gb_to_bb , "BB")
    elif(veri_tipi1 == "GB") and (veri_tipi2 == "GEB"):
        gb_to_geb = veri1 / 11805916e+21
        print(gb_to_geb , "GEB")
    
    if(veri_tipi1 == "TB") and (veri_tipi2 == "GB"):
        tb_to_gb = veri1 * 1024
        print(tb_to_gb , "GB")
    elif(veri_tipi1 == "PB") and (veri_tipi2 == "GB"):
        pb_to_gb = veri1 * 1048576
        print(pb_to_gb , "GB")
    elif(veri_tipi1 == "EB") and (veri_tipi2 == "GB"):
        eb_to_gb = veri1 * 1073741824
        print(eb_to_gb , "GB")
    elif(veri_tipi1 == "ZB") and (veri_tipi2 == "GB"):
        zb_to_gb = veri1 * 10995116e+12
        print(zb_to_gb , "GB")
    elif(veri_tipi1 == "YB") and (veri_tipi2 == "GB"):
        yb_to_gb = veri1 * 11258999e+15
        print(yb_to_gb , "GB")
    elif(veri_tipi1 == "BB") and (veri_tipi2 == "GB"):
        bb_to_gb = veri1 * 11529215e+18
        print(bb_to_gb , "GB")
    elif(veri_tipi1 == "GEB") and (veri_tipi2 == "GB"):
        geb_to_gb = veri1 * 11805916e+21
        print(geb_to_gb , "GB")
    
    if(veri_tipi1 == "TB") and (veri_tipi2 == "PB"):
        tb_to_pb = veri1 / 1024
        print(tb_to_pb , "PB")
    elif(veri_tipi1 == "TB") and (veri_tipi2 == "EB"):
        tb_to_eb = veri1 / 1048576
        print(tb_to_eb , "EB")
    elif(veri_tipi1 == "TB") and (veri_tipi2 == "ZB"):
        tb_to_zb = veri1 / 1073741824
        print(tb_to_zb , "ZB")
    elif(veri_tipi1 == "TB") and (veri_tipi2 == "YB"):
        tb_to_yb = veri1 / 10995116e+12
        print(tb_to_yb , "YB")
    elif(veri_tipi1 == "TB") and (veri_tipi2 == "BB"):
        tb_to_bb = veri1 / 11258999e+15
        print(tb_to_bb , "BB")
    elif(veri_tipi1 == "TB") and (veri_tipi2 == "GEB"):
        tb_to_geb = veri1 / 11529215e+18
        print(tb_to_geb , "GEB")
    
    if(veri_tipi1 == "PB") and (veri_tipi2 == "TB"):
        pb_to_tb = veri1 * 1024
        print(pb_to_tb , "TB")
    elif(veri_tipi1 == "EB") and (veri_tipi2 == "TB"):
        eb_to_tb = veri1 * 1048576
        print(eb_to_tb , "TB")
    elif(veri_tipi1 == "ZB") and (veri_tipi2 == "TB"):
        zb_to_tb = veri1 * 1073741824
        print(zb_to_tb , "TB")
    elif(veri_tipi1 == "YB") and (veri_tipi2 == "TB"):
        yb_to_tb = veri1 * 10995116e+12
        print(yb_to_tb , "TB")
    elif(veri_tipi1 == "BB") and (veri_tipi2 == "TB"):
        bb_to_tb = veri1 * 11258999e+15
        print(bb_to_tb , "TB")
    elif(veri_tipi1 == "GEB") and (veri_tipi2 == "TB"):
        geb_to_tb = veri1 * 11529215e+18
        print(geb_to_tb , "TB")
    
    if(veri_tipi1 == "PB") and (veri_tipi2 == "EB"):
        pb_to_eb = veri1 / 1024
        print(pb_to_eb , "EB")
    elif(veri_tipi1 == "PB") and (veri_tipi2 == "ZB"):
        pb_to_zb = veri1 / 1048576
        print(pb_to_zb , "ZB")
    elif(veri_tipi1 == "PB") and (veri_tipi2 == "YB"):
        pb_to_yb = veri1 / 1073741824
        print(pb_to_yb , "YB")
    elif(veri_tipi1 == "PB") and (veri_tipi2 == "BB"):
        pb_to_bb = veri1 / 10995116e+12
        print(pb_to_bb , "BB")
    elif(veri_tipi1 == "PB") and (veri_tipi2 == "GEB"):
        pb_to_geb = veri1 / 11258999e+15
        print(pb_to_geb , "GEB")
    
    if(veri_tipi1 == "EB") and (veri_tipi2 == "PB"):
        eb_to_pb = veri1 * 1024
        print(eb_to_pb , "PB")
    elif(veri_tipi1 == "ZB") and (veri_tipi2 == "PB"):
        zb_to_pb = veri1 * 1048576
        print(zb_to_pb , "PB")
    elif(veri_tipi1 == "YB") and (veri_tipi2 == "PB"):
        yb_to_pb = veri1 * 1073741824
        print(yb_to_pb , "PB")
    elif(veri_tipi1 == "BB") and (veri_tipi2 == "PB"):
        bb_to_pb = veri1 * 10995116e+12
        print(bb_to_pb , "PB")
    elif(veri_tipi1 == "GEB") and (veri_tipi2 == "PB"):
        geb_to_pb = veri1 * 11258999e+15
        print(geb_to_pb , "PB")
    
    if(veri_tipi1 == "EB") and (veri_tipi2 == "ZB"):
        eb_to_zb = veri1 / 1024
        print(eb_to_zb , "ZB")
    elif(veri_tipi1 == "EB") and (veri_tipi2 == "YB"):
        eb_to_yb = veri1 / 1048576
        print(eb_to_yb , "YB")
    elif(veri_tipi1 == "EB") and (veri_tipi2 == "BB"):
        eb_to_bb = veri1 / 1073741824
        print(eb_to_bb , "BB")
    elif(veri_tipi1 == "EB") and (veri_tipi2 == "GEB"):
        eb_to_geb = veri1 / 10995116e+12
        print(eb_to_geb , "GEB")
    
    if(veri_tipi1 == "ZB") and (veri_tipi2 == "EB"):
        zb_to_eb = veri1 * 1024
        print(zb_to_eb , "EB")
    elif(veri_tipi1 == "YB") and (veri_tipi2 == "EB"):
        yb_to_eb = veri1 * 1048576
        print(yb_to_eb , "EB")
    elif(veri_tipi1 == "BB") and (veri_tipi2 == "EB"):
        bb_to_eb = veri1 * 1073741824
        print(bb_to_eb , "EB")
    elif(veri_tipi1 == "GEB") and (veri_tipi2 == "EB"):
        geb_to_eb = veri1 * 10995116e+12
        print(geb_to_eb , "EB")
    
    if(veri_tipi1 == "ZB") and (veri_tipi2 == "YB"):
        zb_to_yb = veri1 / 1024
        print(zb_to_yb , "YB")
    elif(veri_tipi1 == "ZB") and (veri_tipi2 == "BB"):
        zb_to_bb = veri1 / 1048576
        print(zb_to_bb , "BB")
    elif(veri_tipi1 == "ZB") and (veri_tipi2 == "GEB"):
        zb_to_geb = veri1 / 1073741824
        print(zb_to_geb , "GEB")
    
    if(veri_tipi1 == "YB") and (veri_tipi2 == "ZB"):
        yb_to_zb = veri1 * 1024
        print(yb_to_zb , "ZB")
    elif(veri_tipi1 == "BB") and (veri_tipi2 == "ZB"):
        bb_to_zb = veri1 * 1048576
        print(bb_to_zb , "ZB")
    elif(veri_tipi1 == "GEB") and (veri_tipi2 == "ZB"):
        geb_to_zb = veri1 * 1073741824
        print(geb_to_zb , "ZB")
    
    if(veri_tipi1 == "YB") and (veri_tipi2 == "BB"):
        yb_to_bb = veri1 / 1024
        print(yb_to_bb , "BB")
    elif(veri_tipi1 == "YB") and (veri_tipi2 == "GEB"):
        yb_to_geb = veri1 / 1048576
        print(yb_to_geb , "GEB")
    
    if(veri_tipi1 == "BB") and (veri_tipi2 == "YB"):
        bb_to_yb = veri1 * 1024
        print(bb_to_yb , "YB")
    elif(veri_tipi1 == "GEB") and (veri_tipi2 == "YB"):
        geb_to_yb = veri1 * 1048576
        print(geb_to_yb , "YB")
    
    if(veri_tipi1 == "BB") and (veri_tipi2 == "GEB"):
        bb_to_geb = veri1 / 1024
        print(bb_to_geb , "GEB")
    
    if(veri_tipi1 == "GEB") and (veri_tipi2 == "BB"):
        geb_to_bb = veri1 * 1048576
        print(geb_to_bb , "BB")