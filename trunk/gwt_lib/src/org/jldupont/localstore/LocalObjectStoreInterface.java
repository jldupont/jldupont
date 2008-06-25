/**
 * LocalObjectStoreInterface
 * 
 * @author Jean-Lou Dupont
 */
package org.jldupont.localstore;

import java.lang.String;

public interface LocalObjectStoreInterface {

	public String getTextRepresentation();
	public void   createFromTextRepresentation(String s);

}
