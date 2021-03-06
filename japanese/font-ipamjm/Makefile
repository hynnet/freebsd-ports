# $FreeBSD$

PORTNAME=	ipamjm
PORTVERSION=	00301
CATEGORIES=	japanese x11-fonts
MASTER_SITES=	http://dl.mojikiban.ipa.go.jp/IPAmjMincho/
PKGNAMEPREFIX=	ja-font-
DISTNAME=	${PORTNAME}${PORTVERSION}

MAINTAINER=	hrs@FreeBSD.org
COMMENT=	IPAmj Mincho Japanese fonts

LICENSE=	IPAFLAv1
LICENSE_NAME=	IPA Font License Agreement v1.0
LICENSE_FILE=	${WRKSRC}/IPA_Font_License_Agreement_v1.0.txt
LICENSE_PERMS=	dist-mirror dist-sell pkg-mirror pkg-sell auto-accept

RUN_DEPENDS=	fc-cache:${PORTSDIR}/x11-fonts/fontconfig

USES=		zip
NO_BUILD=	yes
PKGINSTALL=	${WRKDIR}/pkg-install
PKGDEINSTALL=	${WRKDIR}/pkg-install
SUB_FILES=	pkg-install
SUB_LIST=	X_FONTSDIR=${PREFIX}/${X_FONTSDIR}
PLIST_SUB=	X_FONTSDIR=${X_FONTSDIR} \
		LOCAL_FONTSDIR=${LOCAL_FONTSDIR}
DATADIR=	${PREFIX}/share/font-${PORTNAME}
PORTDOCS=	Readme_${PORTNAME}003.01.txt

LOCAL_FONTSDIR=	share/fonts
X_FONTSDIR=	lib/X11/fonts

OPTIONS_DEFINE=	DOCS

.include <bsd.port.options.mk>

do-install:
	${MKDIR} ${STAGEDIR}${DATADIR}
	${INSTALL_DATA} ${WRKSRC}/ipamjm.ttf ${STAGEDIR}${DATADIR}
	${MKDIR} ${STAGEDIR}${PREFIX}/${LOCAL_FONTSDIR}/OTF
	cd ${STAGEDIR}${PREFIX}/${LOCAL_FONTSDIR}/OTF/ && ${LN} -s -f \
	    ../${LOCAL_FONTSDIR:C,[^/]+,..,g}/${DATADIR_REL}/ipamjm.ttf .
	${MKDIR} ${STAGEDIR}${PREFIX}/${X_FONTSDIR}/OTF
	cd ${STAGEDIR}${PREFIX}/${X_FONTSDIR}/OTF/ && ${LN} -s -f \
	    ../${X_FONTSDIR:C,[^/]+,..,g}/${DATADIR_REL}/ipamjm.ttf .
	${MKDIR} ${STAGEDIR}${PREFIX}/etc/fonts/conf.avail \
	    ${STAGEDIR}${PREFIX}/etc/fonts/conf.d
	${INSTALL_DATA} ${FILESDIR}/20-unhint-${PORTNAME}.conf \
	    ${FILESDIR}/62-fonts-${PORTNAME}.conf \
	    ${STAGEDIR}${PREFIX}/etc/fonts/conf.avail
	${LN} -s -f ../conf.avail/20-unhint-${PORTNAME}.conf \
	    ${STAGEDIR}${PREFIX}/etc/fonts/conf.d/20-unhint-${PORTNAME}.conf
	${LN} -s -f ../conf.avail/62-fonts-${PORTNAME}.conf \
	    ${STAGEDIR}${PREFIX}/etc/fonts/conf.d/62-fonts-${PORTNAME}.conf
.if ${PORT_OPTIONS:MDOCS}
	${MKDIR} ${STAGEDIR}${DOCSDIR}
	cd ${WRKSRC} && ${INSTALL_DATA} ${PORTDOCS} ${STAGEDIR}${DOCSDIR}
.endif

.include <bsd.port.mk>
