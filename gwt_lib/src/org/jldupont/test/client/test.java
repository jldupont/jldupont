package org.jldupont.test.client;

import com.google.gwt.core.client.EntryPoint;
import com.google.gwt.user.client.Window;
import com.google.gwt.user.client.ui.Button;
import com.google.gwt.user.client.ui.ClickListener;
import com.google.gwt.user.client.ui.RootPanel;
import com.google.gwt.user.client.ui.Widget;

import org.jldupont.delicious.Tags;

/**
 * Entry point classes define <code>onModuleLoad()</code>.
 */
public class test 
	implements EntryPoint {
	
	private Button clickMeButton;
	
	public static Tags tags;
	
	public void onModuleLoad() {
		
		RootPanel rootPanel = RootPanel.get();

		clickMeButton = new Button();
		rootPanel.add(clickMeButton);
		clickMeButton.setText("Fetch Tags");
		
		tags = new Tags();
		tags.setUser("jldupont");
		
		clickMeButton.addClickListener(new ClickListener() {
			
			public void onClick(Widget sender) {
				test.tags.fetch();
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
