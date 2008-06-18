package com.jldupont.project.client;

import com.google.gwt.core.client.EntryPoint;
import com.google.gwt.user.client.DOM;
import com.google.gwt.user.client.Window;
import com.google.gwt.user.client.Element;
import com.google.gwt.user.client.ui.HasHTML;
import com.google.gwt.user.client.ui.HasName;
import com.google.gwt.user.client.ui.Widget; 

/**
 * Basic implementation of raw Anchor <a> widget
 * @see http://www.w3schools.com/tags/tag_a.asp
 * @author Peter Blazejewicz
 *
 */

public class HTMLLink extends Widget 
	implements HasHTML, HasName, EntryPoint {

  /* ===============================================================================
   *  PROPERTIES
   ===============================================================================*/
	
	
	public void onModuleLoad() {
		
	}
	
  public HTMLLink() {
    setElement(DOM.createAnchor());
  }

  public String getHref() {
    return DOM.getElementAttribute(getElement(), "href");
  }

  public String getHTML() {
    return DOM.getInnerHTML(getElement());
  }

  public String getId() {
    return DOM.getElementAttribute(getElement(), "id");
  }

  public String getName() {
    return DOM.getElementAttribute(getElement(), "name");
  }

  public int getTabIndex() {
    return $getTabIndex(getElement());
  }

  public String getTarget() {
    return DOM.getElementAttribute(getElement(), "target");
  }

  public String getText() {
    return DOM.getInnerText(getElement());
  }

  public void setHref(String href) {
    DOM.setElementAttribute(getElement(), "href", href == null ? "" : href);
  }

  public void setHTML(String html) {
    DOM.setInnerHTML(getElement(), html == null ? "" : html);
  }

  public void setId(String id) {
    DOM.setElementAttribute(getElement(), "id", id == null ? "" : id);
  }

  public void setName(String name) {
    DOM.setElementAttribute(getElement(), "name", name == null ? "" :name);
  }

  public void setTabIndex(int index) {
    $setTabIndex(getElement(), index);
  }

  public void setTarget(String target) {
    DOM.setElementAttribute(getElement(), "target", target == null ? "" : target);
  }

  public void setText(String text) {
    DOM.setInnerText(getElement(), text == null ? "" : text);
  }

  /* ===============================================================================
   *  IMG child node
   ===============================================================================*/
  
  public void setImgUrl(String url ) {
	  // if the img tag isn't created yet, go create it
	  Element $this = getElement();
	  Element img = DOM.getChild( $this, 0);
	  
	  if ( img == null ) {
		  img = DOM.createImg();
		  DOM.insertChild($this, img, 0);
	  } 
	  // set the img tag src attribute
	  DOM.setImgSrc(img, url);
  }
  
  /* ===============================================================================
   *  PRIVATE
   ===============================================================================*/
  
  private native int $getTabIndex(Element element)
  /*-{
      return element.tabIndex;
  }-*/;

  private native void $setTabIndex(Element element, int index)
  /*-{
      element.tabIndex = index;
  }-*/;

}
