/**
 * @file   macros.h
 *
 * @date   2009-05-22
 * @author Jean-Lou Dupont
 */

#ifndef MACROS_H_
#define MACROS_H_


#ifdef _DEBUG
#	define TESTPTR(REF, PTR) if (NULL==PTR) { doLog(LOG_ERR, #REF ": NULL pointer"); cjld_error_set(ECJLD_NULL_POINTER); return 0; }
#else
#	define TESTPTR(REF, PTR) if (NULL==PTR) { cjld_error_set(ECJLD_NULL_POINTER); return 0; }
#endif


#endif /* MACROS_H_ */
