package com.jldupont.project.client;

import com.google.gwt.core.client.EntryPoint;
import com.google.gwt.user.client.Window;
import com.google.gwt.user.client.WindowResizeListener;
import com.google.gwt.user.client.Command;
import com.google.gwt.user.client.DeferredCommand;
import com.google.gwt.user.client.ui.Button;
import com.google.gwt.user.client.ui.ClickListener;
import com.google.gwt.user.client.ui.FlexTable;
import com.google.gwt.user.client.ui.FlowPanel;
import com.google.gwt.user.client.ui.Grid;
import com.google.gwt.user.client.ui.HTML;
import com.google.gwt.user.client.ui.HTMLPanel;
import com.google.gwt.user.client.ui.HasHorizontalAlignment;
import com.google.gwt.user.client.ui.HasVerticalAlignment;
import com.google.gwt.user.client.ui.Hidden;
import com.google.gwt.user.client.ui.HorizontalPanel;
import com.google.gwt.user.client.ui.Hyperlink;
import com.google.gwt.user.client.ui.Image;
import com.google.gwt.user.client.ui.RootPanel;
import com.google.gwt.user.client.ui.TextArea;
import com.google.gwt.user.client.ui.TextBox;
import com.google.gwt.user.client.ui.TextBoxBase;
import com.google.gwt.user.client.ui.VerticalPanel;
import com.google.gwt.user.client.ui.Widget;

/**
 * Entry point classes define <code>onModuleLoad()</code>.
 */
public class main implements EntryPoint, WindowResizeListener {
	
	private FlexTable flexTable = new FlexTable();
	private HTMLLink ImgLinkedin = new HTMLLink();
	private HTMLLink ImgBlog = new HTMLLink();
	private HTMLLink ImgWiki = new HTMLLink();
	private HTMLLink ImgProjects = new HTMLLink();
	private TextBox TextTitle = new TextBox();
	
	public void onModuleLoad() {
		RootPanel.get();
		RootPanel rootPanel = RootPanel.get();
		rootPanel.setSize("100%", "100%");
		rootPanel.setStylePrimaryName("rootPanel");
		rootPanel.setStyleName("rootPanel");

		rootPanel.add(flexTable, 60, 0);
		flexTable.setBorderWidth(2);
		flexTable.setSize("377px", "270px");
		flexTable.setCellSpacing(5);
		flexTable.setCellPadding(5);

		// LinkedIn
		flexTable.setWidget(1, 0, ImgLinkedin);
		flexTable.getCellFormatter().setHorizontalAlignment(1, 0, HasHorizontalAlignment.ALIGN_CENTER);
		ImgLinkedin.setTarget("_blank");
		ImgLinkedin.setHref("http://www.linkedin.com/in/JeanLouDupont");
		ImgLinkedin.setId("link_linkedin");
		ImgLinkedin.setImgUrl("linkedin.gif");

		// Blog
		flexTable.setWidget(1, 1, ImgBlog);
		flexTable.getCellFormatter().setHorizontalAlignment(1, 1, HasHorizontalAlignment.ALIGN_CENTER);
		ImgBlog.setTarget("_blank");
		ImgBlog.setHref("http://jldupont.blogspot.com");
		ImgBlog.setId("link_blog");
		ImgBlog.setImgUrl("blog.jpg");

		// Mediawiki Wiki
		flexTable.setWidget(2, 0, ImgWiki);
		flexTable.getCellFormatter().setHorizontalAlignment(2, 0, HasHorizontalAlignment.ALIGN_CENTER);
		ImgWiki.setTarget("_blank");
		ImgWiki.setHref("http://wiki.jldupont.com");
		ImgWiki.setId("link_wiki");
		ImgWiki.setImgUrl("wiki.png");

		// Projects
		flexTable.setWidget(2, 1, ImgProjects);
		flexTable.getCellFormatter().setHorizontalAlignment(2, 1, HasHorizontalAlignment.ALIGN_CENTER);
		ImgProjects.setTarget("_blank");
		ImgProjects.setHref("http://code.google.com/u/JeanLou.Dupont/");
		ImgProjects.setId("link_projects");
		ImgProjects.setImgUrl("projects.jpg");

		// Title
		flexTable.setWidget(0, 0, TextTitle);
		TextTitle.setStyleName("title");
		TextTitle.setTextAlignment(TextBoxBase.ALIGN_CENTER);
		TextTitle.setTitle("title");
		flexTable.getCellFormatter().setHorizontalAlignment(0, 0, HasHorizontalAlignment.ALIGN_CENTER);
		TextTitle.setText("Jean-Lou Dupont's WEB site");
		flexTable.getFlexCellFormatter().setColSpan(0, 0, 2);
		TextTitle.setWidth("100%");

		final FlexTable flexTableFooter = new FlexTable();
		rootPanel.add(flexTableFooter, 330, 367);
		flexTableFooter.setSize("107px", "40px");

		final Image ImgGwt = new Image();
		flexTableFooter.setWidget(0, 0, ImgGwt);
		flexTableFooter.getCellFormatter().setWidth(0, 0, "43px");
		ImgGwt.setUrl("gwt.png");

		final Image ImgGae = new Image();
		flexTableFooter.setWidget(0, 1, ImgGae);
		flexTableFooter.getCellFormatter().setWidth(0, 1, "50px");
		ImgGae.setUrl("gae.png");
		
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
		
	}

}
