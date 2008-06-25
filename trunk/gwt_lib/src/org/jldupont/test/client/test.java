package org.jldupont.test.client;

import com.google.gwt.core.client.EntryPoint;
import com.google.gwt.user.client.Window;
import com.google.gwt.user.client.ui.Button;
import com.google.gwt.user.client.ui.ClickListener;
import com.google.gwt.user.client.ui.RootPanel;
import com.google.gwt.user.client.ui.Widget;

import org.jldupont.delicious.TagsFetcher;

/**
 * Entry point classes define <code>onModuleLoad()</code>.
 */
public class test 
	implements EntryPoint {
	
	private Button clickMeButton;
	
	public static TagsFetcher tagsFetcher;
	
	public void onModuleLoad() {
		
		RootPanel rootPanel = RootPanel.get();

		clickMeButton = new Button();
		rootPanel.add(clickMeButton);
		clickMeButton.setText("Fetch TagsFetcher");
		
		tagsFetcher = new TagsFetcher();
		tagsFetcher.setUser("jldupont");
		
		clickMeButton.addClickListener(new ClickListener() {
			
			public void onClick(Widget sender) {
				test.tagsFetcher.get();
			}
		});
		
		//testToSource();
		//testObjectLiteral();
		
	}//[onModuleLoad]
	private native void testObjectLiteral() /*-{
	
		var obj = {
			id: "666"
		};
		obj.id2 = function() {
			alert("in obj.id2");
		}
		obj.id2();
}-*/;
	
	
	private native void testToSource() /*-{
		alert( arguments.callee );
		return;
		this.@org.jldupont.test.client.test::test2();
	}-*/;

	private void test2() {
		Window.alert("test2!!");
	}
	
}//end class
