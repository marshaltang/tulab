=================================
非接触APDU指令的模式
=================================

文档编号:ZJJK-3000-XX

.. cssclass:: table-bordered

+-------------------+---------------------+-------------------------------------------+
| 版本信息          |更新日期             | 变更说明                                  |
+===================+=====================+===========================================+
| ZJJK-3000-05-2019 |2021年12月22日       |初始版本                                   |
+-------------------+---------------------+-------------------------------------------+
|                   |2022年6月24日        |add extended指令说明                       |
+-------------------+---------------------+-------------------------------------------+
|                   |2022年7月22日        |READ PICTURE、UPDATE PICTURE 指令sample    |
+-------------------+---------------------+-------------------------------------------+

非接触APDU指令的模式说明
----------------------------------------

以下为JT/T978-2015支持的模式，模式5是模式4情况系Le=00的特例

+------------------+----------------------------+-----+-----+----+----+----+------+----+---------------------------+-------+
| 指令模式         |       指令sample           | CLA | INs | P1 | P2 | Lc | data | Le |预期返回的数据             |SW1SW2 |
+==================+============================+=====+=====+====+====+====+======+====+===========================+=======+
| 指令模式 Case 1  |       算法切换             | CLA | INs | P1 | P2 |null| null |null|null                       |SW1SW2 |
+------------------+----------------------------+-----+-----+----+----+----+------+----+---------------------------+-------+
| 指令模式 Case 2S |       Read binary          | CLA | INs | P1 | P2 |null| null | Le |DATA                       |SW1SW2 |
+------------------+----------------------------+-----+-----+----+----+----+------+----+---------------------------+-------+
| 指令模式 Case 3S | update capp data cache     | CLA | INs | P1 | P2 | Lc | data |null|null                       |SW1SW2 |
+------------------+----------------------------+-----+-----+----+----+----+------+----+---------------------------+-------+
| 指令模式 Case 4S | 5个init和5个交易指令       | CLA | INs | P1 | P2 | Lc | data | Le |DATA                       |SW1SW2 |
+------------------+----------------------------+-----+-----+----+----+----+------+----+---------------------------+-------+
| 指令模式 Case 5S | Select PPSE, Select AID    | CLA | INs | P1 | P2 | Lc | data | 00 |DATA                       |SW1SW2 |
+------------------+----------------------------+-----+-----+----+----+----+------+----+---------------------------+-------+

以下为JT/T978修订新增加的模式 

+---------------------------+-------------------+-----+-----+----+----+----------+-------------------------------------------+----------+---------------------------+-------+
| ISO7816-4 2013 新增       |   指令sample      | CLA | INs | P1 | P2 | Lc       | data                                      | Le       |预期返回的数据             |SW1SW2 |
+===========================+===================+=====+=====+====+====+==========+===========================================+==========+===========================+=======+
| 指令模式 Case 2E xtended  |   READ PICTURE    | CLA | INs | P1 | P2 |null      | null                                      |00+2字节Le|DATA                       |SW1SW2 |
+---------------------------+-------------------+-----+-----+----+----+----------+-------------------------------------------+----------+---------------------------+-------+
| 指令模式 Case 3E xtended  | UPDATE PICTURE    | CLA | INs | P1 | P2 | 2字节Lc  | data                                      |null      |null                       |SW1SW2 |
+---------------------------+-------------------+-----+-----+----+----+----------+-------------------------------------------+----------+---------------------------+-------+
| 指令模式 Case 4E xtended  |                   | CLA | INs | P1 | P2 |00+2字节Lc| data                                      | 2字节Le  |DATA                       |SW1SW2 |
+---------------------------+-------------------+-----+-----+----+----+----------+-------------------------------------------+----------+---------------------------+-------+



钱包应用APDU指令list
----------------------------------------


.. toctree::
   
   ../smartpicc/Select PPSE
   ../smartpicc/Select ADF
   ../smartpicc/READ BINARY
   ../smartpicc/UPDATE BINARY
   ../smartpicc/Read Record
   ../smartpicc/Append Record
   ../smartpicc/UPDATE Record
   ../smartpicc/GET BALANCE
   ../smartpicc/GET CHALLENGE
   ../smartpicc/APPLICATION BLOCK
   ../smartpicc/APPLICATION UNBLOCK
   ../smartpicc/INITIALIZE FOR CAPP PURCHASE
   ../smartpicc/UPDATE CAPP DATA CACHE
   ../smartpicc/DEBIT FOR CAPP PURCHASE
   ../smartpicc/INITIALIZE FOR PURCHASE
   ../smartpicc/DEBIT FOR PURCHASE
   ../smartpicc/INITIALIZE FOR LOAD
   ../smartpicc/CREDIT FOR LOAD
   ../smartpicc/INITIALIZE FOR UNLOAD
   ../smartpicc/DEBIT FOR UNLOAD
   ../smartpicc/INITIALIZE FOR UPDATE
   ../smartpicc/UPDATE OVERDRAW LIMIT
   ../smartpicc/get transaction proof
   ../smartpicc/Get Algorithm
   ../smartpicc/Change Algorithm
   ../smartpicc/Block Algorithm
   ../smartpicc/RELOAD PIN
   ../smartpicc/CHANGE PIN
   ../smartpicc/UNBLOCK PIN
   ../smartpicc/VERIFY PIN
   
   
现金应用APDU指令list
--------------------------

.. Note :: K5应用常用指令

.. toctree::
   
   ../smartpicc/Select PPSE
   ../smartpicc/Select ADF
   ../smartpicc/Read Record
   ../smartpicc/Append Record
   ../smartpicc/UPDATE Record
   ../smartpicc/GET DATA
   ../smartpicc/GET PROCESSING OPTIONS
   ../smartpicc/READ EXT DATA
   ../smartpicc/UPDATE EXT DATA CACHE
   ../smartpicc/get transaction proof
   ../smartpicc/GENERATE AC
   ../smartpicc/GET RESPONSE
   ../smartpicc/PUT DATA
   ../smartpicc/APPLICATION BLOCK
   ../smartpicc/APPLICATION UNBLOCK
   ../smartpicc/EC CHANGE PIN
   ../smartpicc/UNBLOCK PIN
   ../smartpicc/VERIFY PIN
   ../smartpicc/INTERNAL AUTHENTICATE   
   ../smartpicc/EXTERNAL AUTHENTICATE

.. Note :: K5应用新增加的指令

.. toctree:: 
   
   ../smartpicc/READ PICTURE
   ../smartpicc/UPDATE PICTURE
   ../smartpicc/READ QRCODE
