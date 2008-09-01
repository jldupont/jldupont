package com.jldupont.app.DeliciousBrowser.client;

import com.google.gwt.core.client.EntryPoint;
import com.google.gwt.user.client.Window;
import com.google.gwt.user.client.ui.Button;
import com.google.gwt.user.client.ui.ClickListener;
import com.google.gwt.user.client.ui.DeckPanel;
import com.google.gwt.user.client.ui.FlexTable;
import com.google.gwt.user.client.ui.HasVerticalAlignment;
import com.google.gwt.user.client.ui.HorizontalSplitPanel;
import com.google.gwt.user.client.ui.Image;
import com.google.gwt.user.client.ui.RootPanel;
import com.google.gwt.user.client.ui.TabBar;
import com.google.gwt.user.client.ui.TabPanel;
import com.google.gwt.user.client.ui.TextBox;
import com.google.gwt.user.client.ui.VerticalPanel;
import com.google.gwt.user.client.ui.Widget;

/**
 * Entry point classes define <code>onModuleLoad()</code>.
 */
public class main implements EntryPoint {
	public void onModuleLoad() {
		RootPanel rootPanel = RootPanel.get();

		final VerticalPanel verticalPanel = new VerticalPanel();
		rootPanel.add(verticalPanel, 0, 0);
		verticalPanel.setSize("100%", "100%");

		final FlexTable flexTableHeader = new FlexTable();
		verticalPanel.add(flexTableHeader);
		flexTableHeader.setSize("100%", "25");
		verticalPanel.setCellWidth(flexTableHeader, "100%");
		verticalPanel.setCellHeight(flexTableHeader, "25");

		final Image image = new Image();
		flexTableHeader.setWidget(0, 0, image);
		flexTableHeader.getCellFormatter().setWidth(0, 0, "70px");

		final TextBox textBox = new TextBox();
		flexTableHeader.setWidget(0, 1, textBox);
		textBox.setVisibleLength(80);
		textBox.setWidth("100%");

		final HorizontalSplitPanel horizontalSplitPanel = new HorizontalSplitPanel();
		verticalPanel.add(horizontalSplitPanel);
		horizontalSplitPanel.setSize("100%", "100%");
		verticalPanel.setCellHeight(horizontalSplitPanel, "100%");
		verticalPanel.setCellWidth(horizontalSplitPanel, "100%");
		horizontalSplitPanel.setSplitPosition("50%");

		final DeckPanel deckPanel = new DeckPanel();
		horizontalSplitPanel.setLeftWidget(deckPanel);
		deckPanel.setSize("100%", "100%");

		final TabPanel tabPanel = new TabPanel();
		horizontalSplitPanel.setRightWidget(tabPanel);
		tabPanel.selectTab(0);
		tabPanel.setSize("100%", "100%");

		final TabBar tabBar = new TabBar();
		tabPanel.add(tabBar, "Tab");

		final TabBar tabBar_1 = new TabBar();
		tabPanel.add(tabBar_1, "Tab");

		final FlexTable flexTableFooter = new FlexTable();
		verticalPanel.add(flexTableFooter);
		flexTableFooter.setSize("100%", "25");
		verticalPanel.setCellWidth(flexTableFooter, "100%");
		verticalPanel.setCellHeight(flexTableFooter, "25");
	}
}
