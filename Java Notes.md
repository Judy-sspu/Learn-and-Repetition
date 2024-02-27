Java语言高级-02继承与多态-第三节接口

接口的默认方法定义

package Demo01;

/*
从Java 8开始，接口允许定义默认方法
格式：
public default 返回值类型 方法名称(参数列表){
	方法体
}

备注：接口当中默认的方法，可以解决接口升级的问题。

 */
public interface MyInterfaceDefault {
	//抽象方法	
	public abstract void methodAbs();
	
	//新添加了一个抽象方法
	public abstract void methodAbs2();
	
}


package Demo01;

public class MyInterfaceDefaultA  implements MyInterfaceDefault{

	@Override
	public void methodAbs() {
		// TODO Auto-generated method stub
		System.out.println("实现了抽象方法，AAA");
	}
	
}

package Demo01;

public class MyInterfaceDefaultB  implements MyInterfaceDefault{

	@Override
	public void methodAbs() {
		// TODO Auto-generated method stub
		System.out.println("实现了抽象方法，BBB");
	}
	
}
