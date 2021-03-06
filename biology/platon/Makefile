# Created by: Ryo MIYAMOTO <rmiya@cc.hirosaki-u.ac.jp>
# $FreeBSD$

PORTNAME=	platon
PORTVERSION=	2014.07.13
PORTREVISION=	1
CATEGORIES=	biology
# Please note that the upstream vendor does not perform any discernible
# versioning. Therefore, the distfile has to be hosted elsewhere in order
# to prevent breakage due to distinfo becoming outdated unexpectedly. For the
# latest upstream version, please see
# http://www.cryst.chem.uu.nl/spek/xraysoft/unix/
MASTER_SITES=	http://www.skysmurf.nl/comp/FreeBSD/distfiles/
DISTNAME=	platon

MAINTAINER=	ports@FreeBSD.org
COMMENT=	Tool for viewing molecular/crystallographic structures

BROKEN=		Unfetchable
# PLATON may be used free of charge by the academic community under
# the condition that it is not redistributed for a current & fresh copy.
# There is a charge of US$ 5000 for commercial users.
RESTRICTED=	free for academic, US$ 5000 for commercial users

USES=		fortran
USE_XORG=	x11

SAMPLES=	azt.dat bucky.spf c476.spf c540.cart3d check.def cubane.spf \
		cyto.spf ml.pdb s810c.cif s913a.res sucrose.spf
TESTDATADIR=	ABSORB_EXAMPLE ABSTOMPA_EXAMPLE ABSTOMPA_TEST ADDSYM_EXAMPLE \
		ASYM_EXAMPLE MULABS_EXAMPLE PSICOR_EXAMPLE SQUEEZE_EXAMPLE

OPTIONS_DEFINE=	DOCS

.include <bsd.port.pre.mk>

pre-patch:
	(cd ${WRKDIR}/${DISTNAME} ; ${GUNZIP_CMD} platon.f.gz xdrvr.c.gz)

post-patch:
	${CP} ${FILESDIR}/Makefile ${WRKSRC}/Makefile
	${REINPLACE_CMD} -e "s+%%LOCALBASE%%+${LOCALBASE}+"  ${WRKSRC}/Makefile

do-install:
	${INSTALL_PROGRAM} ${WRKDIR}/${DISTNAME}/platon \
		${STAGEDIR}${PREFIX}/bin
	${LN} -s platon ${STAGEDIR}${PREFIX}/bin/pluton
	${MKDIR} ${STAGEDIR}${DOCSDIR}
	${INSTALL_DATA} ${WRKDIR}/${DISTNAME}/README* ${STAGEDIR}${DOCSDIR}
.for f in ${SAMPLES}
	${INSTALL_DATA} ${WRKDIR}/${DISTNAME}/$f ${STAGEDIR}${DOCSDIR}
.endfor
	${INSTALL_DATA} ${WRKDIR}/${DISTNAME}/platon_html.tar.gz \
		${STAGEDIR}${DOCSDIR}
	${MKDIR} ${STAGEDIR}${DOCSDIR}/TEST
.for d in ${TESTDATADIR}
	${MKDIR} ${STAGEDIR}${DOCSDIR}/TEST/$d
	${INSTALL_DATA} ${WRKDIR}/${DISTNAME}/TEST/$d/* \
		${STAGEDIR}${DOCSDIR}/TEST/$d
.endfor

.include <bsd.port.post.mk>
