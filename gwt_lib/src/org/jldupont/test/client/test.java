/**
 * @author Jean-Lou Dupont
 * 
 *  Serves as test for the librairy
 */
package org.jldupont.test.client;

import com.google.gwt.core.client.EntryPoint;
import com.google.gwt.user.client.Window;
import com.google.gwt.user.client.ui.Button;
import com.google.gwt.user.client.ui.ClickListener;
import com.google.gwt.user.client.ui.ListBox;
import com.google.gwt.user.client.ui.RootPanel;
import com.google.gwt.user.client.ui.Widget;

import org.jldupont.delicious.TagsFetcher;
import org.jldupont.system.Factory;

/**
 * Entry point classes define <code>onModuleLoad()</code>.
 */
public class test 
	implements EntryPoint {
	
	private Button clickMeButton;
	
	public static TagsFetcher tagsFetcher;
	
	protected TagsChangedListenerTest tagsChangedListener = null;
	
	public void onModuleLoad() {
		
		RootPanel rootPanel = RootPanel.get();

		clickMeButton = new Button();
		rootPanel.add(clickMeButton);
		clickMeButton.setText("Fetch TagsFetcher");
		
		tagsFetcher = (org.jldupont.delicious.TagsFetcher) Factory.create("org.jldupont.delicious.TagsFetcher");
		tagsFetcher.setUser("jldupont");
		
		this.tagsChangedListener = new TagsChangedListenerTest();
		
		tagsFetcher.addCallListener(this.tagsChangedListener);
		
		clickMeButton.addClickListener(new ClickListener() {
			
			public void onClick(Widget sender) {
				test.tagsFetcher.get();
			}
		});

		final ListBox listBox = new ListBox();
		rootPanel.add(listBox, 5, 48);
		listBox.setSize("87px", "228px");
		listBox.setVisibleItemCount(5);
		
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
