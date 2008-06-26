/**
 * Delicious Browser
 * GWT
 * 
 * @author Jean-Lou Dupont
 */
package com.jldupont.project.client;

import org.jldupont.system.*;
import org.jldupont.delicious.TagsFetcher;
import org.jldupont.browser.Param;
import org.jldupont.browser.URLParamsList;

import com.google.gwt.user.client.Element;
import com.google.gwt.user.client.DOM;

import com.google.gwt.core.client.EntryPoint;
import com.google.gwt.user.client.Command;
import com.google.gwt.user.client.DeferredCommand;
import com.google.gwt.user.client.Window;
import com.google.gwt.user.client.WindowResizeListener;

import com.google.gwt.user.client.ui.FlexTable;
import com.google.gwt.user.client.ui.Frame;
import com.google.gwt.user.client.ui.HasHorizontalAlignment;
import com.google.gwt.user.client.ui.HasVerticalAlignment;
import com.google.gwt.user.client.ui.Image;
import com.google.gwt.user.client.ui.Label;
import com.google.gwt.user.client.ui.ListBox;
import com.google.gwt.user.client.ui.RootPanel;
import com.google.gwt.user.client.ui.TextBox;
import com.google.gwt.user.client.ui.TextBoxBase;


/**
 * Entry point classes define <code>onModuleLoad()</code>.
 */
public class main implements EntryPoint, WindowResizeListener {
	
	/**
	 * Controls
	 */
	final FlexTable flexTable = new FlexTable();
	final ListBox lbTags = new ListBox();	
	final ListBox lbPosts = new ListBox();
	final Frame frPost = new Frame("");
	final Frame frTags = new Frame("");
	final Frame frPosts = new Frame("");
	final TextBox ftTags = new TextBox();
	final TextBox ftPosts = new TextBox();

	final Label labelUser = new Label("User:");	
	final TextBox tbUser = new TextBox();	
	/**
	 * List of valid Parameters
	 */
	String[] validParams = {
		"u", "tf", "pf",
	};
	
	/**
	 * List of parameters
	 */
	URLParamsList params;
	
	/*
	 * (non-Javadoc)
	 * @see com.google.gwt.core.client.EntryPoint#onModuleLoad()
	 */
	public void onModuleLoad() {
		RootPanel rootPanel = RootPanel.get();

		
		rootPanel.add(flexTable, 0, 0);
		flexTable.setSize("100%", "100%");

		flexTable.setWidget(3, 0, lbTags);
		flexTable.getCellFormatter().setWidth(3, 0, "10%");
		flexTable.getCellFormatter().setVerticalAlignment(3, 0, HasVerticalAlignment.ALIGN_TOP);
		lbTags.setSize("100%", "100%");		
		lbTags.setVisibleItemCount(100);
		
		flexTable.setWidget(3, 1, lbPosts);
		flexTable.getCellFormatter().setWidth(3, 1, "10%");
		flexTable.getCellFormatter().setVerticalAlignment(3, 1, HasVerticalAlignment.ALIGN_TOP);
		lbPosts.setVisibleItemCount(100);
		lbPosts.setSize("100%", "100%");

		flexTable.setWidget(3, 2, frPost);
		flexTable.getCellFormatter().setWidth(3, 2, "80%");
		frPost.setSize("100%", "100%");


		flexTable.setWidget(2, 0, ftTags);
		ftTags.setSize("100%", "100%");
		flexTable.getCellFormatter().setHeight(2, 0, "34px");


		flexTable.setWidget(2, 1, ftPosts);
		ftPosts.setSize("100%", "100%");

		flexTable.setWidget(1, 0, labelUser);
		flexTable.getCellFormatter().setHorizontalAlignment(1, 0, HasHorizontalAlignment.ALIGN_RIGHT);
		labelUser.setSize("100%", "100%");
		flexTable.getCellFormatter().setHeight(1, 0, "27px");


		flexTable.setWidget(1, 1, tbUser);
		tbUser.setSize("100%", "100%");
		tbUser.setTitle("UserName");
		tbUser.setTextAlignment(TextBoxBase.ALIGN_LEFT);

		final FlexTable header = new FlexTable();
		flexTable.setWidget(0, 0, header);
		flexTable.getCellFormatter().setHeight(0, 0, "52px");
		flexTable.getFlexCellFormatter().setColSpan(0, 0, 3);

		final Image image = new Image();
		flexTable.setWidget(0, 3, image);
		image.setUrl("gears_logo_grey.gif");

		
		rootPanel.add(frPosts, 571, 577);
		frPosts.setSize("12px", "6px");
		frPosts.setVisible(false);
		
		this.params = new URLParamsList();
		
		String liste=new String("");
		
		Param param;
		
		while( this.params.hasNext() ) {
			
			param = (Param) this.params.next();
			
			liste += "name: " + param.getName() + " value: " + param.getValue();
		}
		
		if ( liste.length() != 0 ) {
			Logger.log( "Parameters:: " + liste );
		}
		//Window.alert( "Parameters:: " + liste );
		
	    DeferredCommand.addCommand(new Command() {
	        public void execute() {
	          onWindowResized(Window.getClientWidth(), Window.getClientHeight());
	        }
	      });

	    onWindowResized(Window.getClientWidth(), Window.getClientHeight());
	    
	    doTest();

	}
	
	/*TODO
	 * (non-Javadoc)
	 * @see com.google.gwt.user.client.WindowResizeListener#onWindowResized(int, int)
	 */
	public void onWindowResized(int width, int height) {
		
		Element ft = flexTable.getElement();
		
		int ww = this.flexTable.getOffsetWidth();
		
		int l = width - ww;

		DOM.setStyleAttribute(ft, "position", "absolute");
		DOM.setStyleAttribute(ft, "left", l + "px");
	}

	private void doTest() {

		String id;
		
		TagsFetcher t1 = (TagsFetcher) Factory.create( "org.jldupont.delicious.TagsFetcher", "id1" );
		t1.recycle();
		
		TagsFetcher t2 = (TagsFetcher) Factory.create( "org.jldupont.delicious.TagsFetcher", "id2" );
		t2.recycle();
	}
	
}//end class
