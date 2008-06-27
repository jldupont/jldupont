/**
 * GWT - www.jldupont.com
 * 
 * @author Jean-Lou Dupont
 */
package com.jldupont.project.client;

import com.google.gwt.user.client.Element;
import com.google.gwt.user.client.DOM;
import com.google.gwt.core.client.EntryPoint;
import com.google.gwt.user.client.Window;
import com.google.gwt.user.client.WindowResizeListener;
import com.google.gwt.user.client.Command;
import com.google.gwt.user.client.DeferredCommand;
import com.google.gwt.user.client.ui.FlexTable;
import com.google.gwt.user.client.ui.HasHorizontalAlignment;
import com.google.gwt.user.client.ui.Image;
import com.google.gwt.user.client.ui.RootPanel;
import com.google.gwt.user.client.ui.TextBox;
import com.google.gwt.user.client.ui.TextBoxBase;

import org.jldupont.widget.ImgAnchorLink;

/**
 * Entry point classes define <code>onModuleLoad()</code>.
 */
public class main implements EntryPoint, WindowResizeListener {
	
	private FlexTable flexTable = new FlexTable();
	private ImgAnchorLink ImgLinkedin = new ImgAnchorLink();
	private ImgAnchorLink ImgBlog = new ImgAnchorLink();
	private ImgAnchorLink ImgWiki = new ImgAnchorLink();
	private ImgAnchorLink ImgProjects = new ImgAnchorLink();
	private TextBox TextTitle = new TextBox();
	
	public void onModuleLoad() {
		RootPanel.get();
		RootPanel rootPanel = RootPanel.get();
		rootPanel.setSize("100%", "100%");
		rootPanel.setStylePrimaryName("rootPanel");
		rootPanel.setStyleName("rootPanel");

		rootPanel.add(flexTable, 60, 0);
		flexTable.setStyleName("gwt-TabPanel");
		flexTable.setBorderWidth(1);
		flexTable.setSize("377px", "270px");
		flexTable.setCellSpacing(5);
		flexTable.setCellPadding(5);

		// LinkedIn
		flexTable.setWidget(1, 0, ImgLinkedin);
		ImgLinkedin.setStylePrimaryName("gwt-Image");
		flexTable.getCellFormatter().setHorizontalAlignment(1, 0, HasHorizontalAlignment.ALIGN_CENTER);
		ImgLinkedin.setTarget("_blank");
		ImgLinkedin.setHref("http://www.linkedin.com/in/JeanLouDupont");
		ImgLinkedin.setId("link_linkedin");
		ImgLinkedin.setImgUrl("linkedin.gif");
		ImgLinkedin.setImgClass("gwt-Image");
		ImgLinkedin.setTitle("my LinkedIn profile");

		// Blog
		flexTable.setWidget(1, 1, ImgBlog);
		ImgBlog.setStylePrimaryName("gwt-Image");
		ImgBlog.setImgClass("gwt-Image");
		flexTable.getCellFormatter().setHorizontalAlignment(1, 1, HasHorizontalAlignment.ALIGN_CENTER);
		ImgBlog.setTarget("_blank");
		ImgBlog.setHref("http://jldupont.blogspot.com");
		ImgBlog.setId("link_blog");
		ImgBlog.setImgUrl("blog.jpg");
		ImgBlog.setTitle("my WEBlog");		

		// Mediawiki Wiki
		flexTable.setWidget(2, 0, ImgWiki);
		ImgWiki.setStylePrimaryName("gwt-Image");
		ImgWiki.setImgClass("gwt-Image");
		flexTable.getCellFormatter().setHorizontalAlignment(2, 0, HasHorizontalAlignment.ALIGN_CENTER);
		ImgWiki.setTarget("_blank");
		ImgWiki.setHref("http://wiki.jldupont.com");
		ImgWiki.setId("link_wiki");
		ImgWiki.setImgUrl("wiki.png");
		ImgWiki.setTitle("my Mediawiki site & extensions");

		// Projects
		flexTable.setWidget(2, 1, ImgProjects);
		ImgProjects.setStylePrimaryName("gwt-Image");
		ImgProjects.setImgClass("gwt-Image");
		flexTable.getCellFormatter().setHorizontalAlignment(2, 1, HasHorizontalAlignment.ALIGN_CENTER);
		ImgProjects.setTarget("_blank");
		ImgProjects.setHref("http://code.google.com/u/JeanLou.Dupont/");
		ImgProjects.setId("link_projects");
		ImgProjects.setImgUrl("projects.jpg");
		ImgProjects.setTitle("my open projects");

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
		flexTable.setWidget(3, 0, flexTableFooter);
		flexTable.getCellFormatter().setHorizontalAlignment(3, 0, HasHorizontalAlignment.ALIGN_CENTER);
		flexTable.getFlexCellFormatter().setColSpan(3, 0, 2);

		final Image ImgGwt = new Image();
		flexTableFooter.setWidget(0, 0, ImgGwt);
		flexTableFooter.getCellFormatter().setWidth(0, 0, "43px");
		ImgGwt.setUrl("gwt.png");
		ImgGwt.setTitle("built using GoogleWebToolkit");

		final Image ImgGae = new Image();
		flexTableFooter.setWidget(0, 1, ImgGae);
		flexTableFooter.getCellFormatter().setWidth(0, 1, "50px");
		ImgGae.setUrl("gae.png");
		ImgGae.setTitle("built using GoogleAppEngine");
		
	    DeferredCommand.addCommand(new Command() {
	        public void execute() {
	          onWindowResized(Window.getClientWidth(), Window.getClientHeight());
	        }
	      });

	    onWindowResized(Window.getClientWidth(), Window.getClientHeight());
		
	    Window.addWindowResizeListener(this);
	    
	}
		/*TODO
		 * (non-Javadoc)
		 * @see com.google.gwt.user.client.WindowResizeListener#onWindowResized(int, int)
		 */
	public void onWindowResized(int width, int height) {
		
		Element ft = flexTable.getElement();
		
		int ww = this.flexTable.getOffsetWidth();
		
		int l = (width - ww) / 2;

		DOM.setStyleAttribute(ft, "position", "absolute");
		DOM.setStyleAttribute(ft, "left", l + "px");	
	}

}
