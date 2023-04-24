=================================
刷卡终端应用软件入网测试作业指导
=================================

文档编号:ZJJK-3000-05

.. cssclass:: table-bordered

+-------------------+---------------------+-------------------------------------------+
| 版本信息          |更新日期             | 变更说明                                  |
+===================+=====================+===========================================+
| ZJJK-3000-05-2019 |2019年7月1日         |初始版本                                   |
+-------------------+---------------------+-------------------------------------------+
| ZJJK-3000-05-2021 |2021年9月9日         |调整案例说明链接                           |
+-------------------+---------------------+-------------------------------------------+


SmartPICC实现框架
-------------------------------

.. Note :: SmartPICC实现框架

.. mermaid::

   sequenceDiagram
    participant HSM
	participant 云SE服务
    participant SmartPICC
    participant Validator
    participant PSAM
	
	
	云SE服务->>HSM:对称密钥计算请求
	
	HSM->>云SE服务:对称密钥计算响应
	
	云SE服务->>HSM:非对称密钥计算请求
	
	HSM->>云SE服务:非对称密钥计算响应
	
	loop 云SE服务
        云SE服务-->>云SE服务:通过电子票卡应用数据准备系统生成相关数据
    end
	
	SmartPICC->>云SE服务:数据下发请求
	
	云SE服务->>SmartPICC:数据下发响应
	
	SmartPICC->>云SE服务:密钥下发请求
	
	云SE服务->>SmartPICC:密钥下发响应
	
	loop SmartPICC
        SmartPICC-->>SmartPICC:通过HCE方式在REE环境下实现NFC虚拟卡应用服务
    end
	
	Validator->>SmartPICC:票卡应用选择请求
	
	SmartPICC->>Validator:票卡应用选择响应
	
	Validator->>SmartPICC:票卡应用指令1请求
	
	SmartPICC->>Validator:票卡应用指令1响应
	
	
	Validator->>PSAM:PSAM应用辅助验证请求
	
	PSAM->>Validator:PSAM应用辅助验证响应
	
	
	
	Validator->>SmartPICC:票卡应用指令n请求
	
	SmartPICC->>Validator:票卡应用指令n响应
	
	SmartPICC->>云SE服务:检票数据上送	

SmartPICC软件使用说明
----------------------------------------

.. Note :: 见实验室作业指导

https://kdocs.cn/l/cj16lDyXmAIy
	

刷卡终端要求
----------------------------------------

.. Note :: 参考刷卡终端入网送检指南

.. toctree::
   :maxdepth: 1
   
   ../terminalsetting/README

   

	
入网测试案例（kernel1）
------------------------

.. toctree::
   :maxdepth: 1

   ../kernel1/README

入网测试案例（kernel2）
------------------------

.. toctree::
   :maxdepth: 1

   ../kernel2/README

入网测试案例（kernel3）
------------------------

.. toctree::
   :maxdepth: 1

   ../kernel3/README

入网测试案例（kernel4）
------------------------

.. toctree::
   :maxdepth: 1

   ../kernel4/README

入网测试案例（kernel5）
------------------------

.. toctree::
   :maxdepth: 1

   ../kernel5/README

入网测试案例（kernel6）
------------------------

.. toctree::
   :maxdepth: 1

   ../kernel6/README






