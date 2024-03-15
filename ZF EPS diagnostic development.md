诊断开发说明

网关盒子开发流程

客户方需求提出
pil、EPM整理CAN matrix，CANalyzer、CANape、dbc、a2l等文件，并和开发工程师核对，确认后进行正式开发，并同时让技术员根据接口的PIN定义去制作网关盒子
编写C语言程序，并在hightec环境中编译hex文件，使用英飞凌工具刷入网关盒电路板中，
测试：连接硬件，构成硬件在环系统，在上位机中打开CANalyzer、CANape等工程，并观察CANalyzer报文的收发情况，和CANape中变量的读取情况
如果和matrix中结果不对，需要修改程序重新编译，检查转角、车速、引擎状态等信息，并拧动EPS，检查是否有助力
测试报告编写
硬件发货给客户

客户方如果还有问题的话，我们这边会先检测硬件连接是否正确，或者分析之前录制的blf并和客户给的blf信息进行比对，查找原因，定位问题，
修改代码。以客户方的需求为主。


项目架构介绍

转向系统
采购 网关盒子，线束，烧录器等硬件原件
工具组 负责网关盒软件开发，以及VN89开发
刷件组 负责刷程序到EPS中

个人角色说明 网关盒子软件开发，测试，报告编写



网关盒子硬件说明

网关盒 DB9口 2低7高 1低8高
电源线： 蓝 IG 黄 GND 棕 +12V
整车线： 蓝 CAN高 棕 CAN低 信号从整车端输入
EPS线： 蓝 CAN高 棕 CAN低 黄色 IG 信号从EPS侧输出

网关盒子的作用：在整车端和EPS侧充当一个枢纽的作用，中转信号

![Gateway Box Signal Flow](https://github.com/Judy-sspu/Judy-s-Own-Repository/blob/master/Picture1.png)

代码编写过程中遇到的问题:
周期没有设置正确
节点分配错误，通道分配错误
信号值定义的位值过少，导致溢出，与预期结果不匹配
节点的波特率设置不对，导致没有收到信号或者不能发出信号
CRC 和 counter设置不对导致没有助力
发送函数写错，导致CANfd报文后8字节以后的字节全部为0，无法传值出来
多条报文设置的收发关系设置不对，导致EPS的助力不完全

如何判断自己的代码有问题？
程序刷入网关盒子之后，在CANalyzer中观察报文的周期、通道、报文类型、Data段数据、以及报文中的信号值，比对是否达到了预期
值，如果没有达到预期值，进一步定位错位类型，然后定位到某条报文所在的程序行，查看传值是否有误，并修改程序。

如何判断checksum和crc没有问题？
checksum和crc的作用是对报文的其他字节进行数据校验，用于检测数据在传输或存储过程中是否发生了错误或变化。
首先直接连EPS不连网关盒子，开启CANalyzer录制一个blf文件，记录下其中某条报文的每个counter值所对应的checksum值
然后连网关盒子，同样录制一个blf文件，记录同样一条报文的counter所对应的crc值，继续比对2次操作下来的crc和counter
是否一致，一致则说明crc算法逻辑在程序中没有问题。





总线协议: CAN CANfd LIN Flexray J1939 XCP DoIP SOME/IP SPI I2C UDS ETH UArt TCP/IP

软件工具使用：CANalyzer/CANoe CANape Matlab(simulnk模块)

硬件工具使用：热风枪、电烙铁、万用表、示波器、VN1610、VN1630、VN1640、VN7640、VN8911

编程语言：C/C++ Capl (python/java/shell 选择）

其他：Linux命令，git命令（版本管理）、数据结构与算法、操作系统、雅思或者托福(目前六级通过了)

项目管理：测试周期(1个月)，测试的架构，Aspice开发流程，ISO26262功能安全

Aspice开发流程   
客户需求审计:根据客户需求识别软件设计模型并制定计划;   
设计审核:根据客户需求分析、设计和实现软件解决方案;   
开发审核:通过开发组件、子系统和单元测试进行软件组装;   
集成审核:确定软件系统测试策略并完成软件集成测试;   
系统审计:完成软件系统测试、纠错和软件系统的优化;   
发布审核:确保软件产品的可靠可用性;   
后期维护:确保不断改进软件产品质量符合客户需求   


Diagnostic development instructions

Gateway Box Development Process

Customer demand proposal

PIL and EPM organize CAN matrix, CANalyzer, CANape, dbc, a2l and other files, and verify them with the development engineer before proceeding with formal development. At the same time, let the technician create the gateway box according to the PIN definition of the interface
Write a C language program and compile hex files in the hightec environment. Use Infineon tools to flash into the gateway box circuit board,

Test: 
Connect hardware to form a hardware in the loop system, open projects such as CANalyzer and CANape in the morning machine, and observe the transmission and reception of CANalyzer messages and the reading of variables in CANape
If the results in the matrix are not correct, the program needs to be modified and recompiled to check information such as steering angle, vehicle speed, engine status, etc., and EPS needs to be twisted to check for assistance

Test report writing

Hardware shipment to customers
If the customer still has any issues, we will first check whether the hardware connection is correct, or analyze the previously recorded BLF and compare it with the BLF information provided by the customer to find the cause and locate the problem,
Modify the code. Based on the needs of the client.
Introduction to Project Architecture

steering system 

Purchase hardware components such as gateway boxes, wiring harnesses, burners, etc
The tool group is responsible for gateway box software development and VN89 development
The brushing group is responsible for brushing the program into EPS
Personal Role Description Gateway Box Software Development, Testing, and Report Writing

Gateway Box Hardware Description

Gateway box DB9 port 2 low 7 high 1 low 8 high

Power cord: 

blue IG, yellow GND, brown+12V

Vehicle line:

Blue CAN high brown CAN low signal input from the vehicle end

EPS line: 

Blue CAN high brown CAN low yellow IG signal output from EPS side

The function of the gateway box is to serve as a hub at the vehicle end and EPS side, serving as a relay signal
! [Gateway Box Signal Flow]（ https://github.com/Judy-sspu/Judy-s-Own-Repository/blob/master/Picture1.png ）
Problems encountered during the code writing process:

The cycle was not set correctly

Node allocation error, channel allocation error

The signal value defines too few bit values, resulting in overflow and mismatch with expected results

The baud rate of the node is not set correctly, resulting in no signal being received or no signal being emitted

Incorrect CRC and counter settings result in no assistance

The sending function was written incorrectly, resulting in all bytes after the last 8 bytes of the CANfd message being 0 and unable to transmit a value

The incorrect sending and receiving relationship settings for multiple messages result in incomplete assistance from EPS
How to determine if there is a problem with your code?

After the program is flushed into the gateway box, observe the cycle, channel, message type, Data segment data, and signal value of the message in the CANalyzer to compare whether it meets the expected results

If the expected value is not reached, further locate the misalignment type, then locate the program line where a certain message is located, check for errors in the value passed, and modify the program.

How to determine if there are no issues with checksum and CRC?

The function of checksum and CRC is to perform data verification on other bytes of the message, used to detect whether there have been errors or changes in the data during transmission or storage.

First, connect directly to EPS without connecting to the gateway box. Open CANalyzer to record a BLF file and record the checksum value corresponding to each counter value of a certain message

Then connect to the gateway box, record a BLF file, record the CRC value corresponding to the counter of the same message, and continue comparing the CRC and counter after two operations

Is it consistent? Consistent indicates that the logic of the CRC algorithm is not a problem in the program.











