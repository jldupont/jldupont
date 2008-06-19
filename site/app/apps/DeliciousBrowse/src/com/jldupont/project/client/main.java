/**
 * Delicious Browser
 * GWT
 * 
 * @author Jean-Lou Dupont
 */
package com.jldupont.project.client;

import com.jldupont.project.client.Param;
import com.jldupont.project.client.ParamsList;

import com.google.gwt.user.client.Element;
import com.google.gwt.user.client.DOM;

import com.google.gwt.core.client.EntryPoint;
import com.google.gwt.user.client.Command;
import com.google.gwt.user.client.DeferredCommand;
import com.google.gwt.user.client.Window;
import com.google.gwt.user.client.WindowResizeListener;
import com.google.gwt.user.client.ui.AbsolutePanel;
import com.google.gwt.user.client.ui.Button;
import com.google.gwt.user.client.ui.ClickListener;

import com.google.gwt.user.client.ui.FlexTable;
import com.google.gwt.user.client.ui.Frame;
import com.google.gwt.user.client.ui.HasHorizontalAlignment;
import com.google.gwt.user.client.ui.HasVerticalAlignment;
import com.google.gwt.user.client.ui.Label;
import com.google.gwt.user.client.ui.ListBox;
import com.google.gwt.user.client.ui.RootPanel;
import com.google.gwt.user.client.ui.TextBox;
import com.google.gwt.user.client.ui.TextBoxBase;
import com.google.gwt.user.client.ui.Widget;

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
	final Frame frPost = new Frame("http://www.jldupont.com");
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
	ParamsList params;
	
	/*
	 * (non-Javadoc)
	 * @see com.google.gwt.core.client.EntryPoint#onModuleLoad()
	 */
	public void onModuleLoad() {
		RootPanel rootPanel = RootPanel.get();

		
		rootPanel.add(flexTable, 0, 0);
		flexTable.setSize("100%", "100%");

		flexTable.setWidget(2, 0, lbTags);
		flexTable.getCellFormatter().setWidth(2, 0, "10%");
		flexTable.getCellFormatter().setVerticalAlignment(2, 0, HasVerticalAlignment.ALIGN_TOP);
		lbTags.setSize("100%", "100%");		
		lbTags.setVisibleItemCount(100);
		
		flexTable.setWidget(2, 1, lbPosts);
		flexTable.getCellFormatter().setWidth(2, 1, "10%");
		flexTable.getCellFormatter().setVerticalAlignment(2, 1, HasVerticalAlignment.ALIGN_TOP);
		lbPosts.setVisibleItemCount(100);
		lbPosts.setSize("100%", "100%");

		flexTable.setWidget(2, 2, frPost);
		flexTable.getCellFormatter().setWidth(2, 2, "80%");
		frPost.setSize("100%", "100%");


		flexTable.setWidget(1, 0, ftTags);
		ftTags.setSize("100%", "100%");
		flexTable.getCellFormatter().setHeight(1, 0, "34px");


		flexTable.setWidget(1, 1, ftPosts);
		ftPosts.setSize("100%", "100%");

		flexTable.setWidget(0, 0, labelUser);
		flexTable.getCellFormatter().setHorizontalAlignment(0, 0, HasHorizontalAlignment.ALIGN_RIGHT);
		labelUser.setSize("100%", "100%");
		flexTable.getCellFormatter().setHeight(0, 0, "27px");


		flexTable.setWidget(0, 1, tbUser);
		tbUser.setSize("100%", "100%");
		tbUser.setTitle("UserName");
		tbUser.setTextAlignment(TextBoxBase.ALIGN_LEFT);

		
		rootPanel.add(frPosts, 571, 577);
		frPosts.setSize("12px", "6px");
		frPosts.setVisible(false);
		
		this.params = new ParamsList();
		
		String liste=new String("");
		
		Param param;
		
		while( this.params.hasNext() ) {
			
			param = (Param) this.params.next();
			
			liste += "name: " + param.getName() + " value: " + param.getValue();
		}
		
		if ( liste.length() != 0 )
			Window.alert( "Parameters:: " + liste );
		
	    DeferredCommand.addCommand(new Command() {
	        public void execute() {
	          onWindowResized(Window.getClientWidth(), Window.getClientHeight());
	        }
	      });

	    onWindowResized(Window.getClientWidth(), Window.getClientHeight());

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
	
}//end class
