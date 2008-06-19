package com.jldupont.project.client;

public class Param 
	extends Object {
	
	String name;
	String value;
	
	Param( String name, String value ) {
		this.name = new String( name );
		this.value = new String( value );
	}
	
	public String getName() {
		return this.name;
	}
	
	public String getValue() {
		return this.value;
	}
}//endclass