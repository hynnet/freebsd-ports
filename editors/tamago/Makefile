# Created by: tetsushi NAKAI <nakai@tsl.pe.u-tokyo.ac.jp>
# $FreeBSD$

PORTNAME=	tamago
PORTVERSION=	4.0.6.0.20041122.19
PORTREVISION=	12
CATEGORIES=	editors elisp
MASTER_SITES=	${MASTER_SITE_DEBIAN}
MASTER_SITE_SUBDIR=	pool/main/e/egg
PKGNAMESUFFIX=	-${EMACS_PORT_NAME}
DISTNAME=	egg_4.0.6+0.20041122cvs.orig

PATCH_SITES=	${MASTER_SITE_DEBIAN:S,%SUBDIR%,pool/main/e/egg,} \
		${MASTER_SITE_LOCAL:S,%SUBDIR%,nork,}
PATCHFILES=	egg_4.0.6+0.20041122cvs-19.diff.gz
PATCH_DIST_STRIP=	-p1

MAINTAINER=	hrs@FreeBSD.org
COMMENT=	Egg V4, Multilingual Input Method for Emacsen

LICENSE=	GPLv2

USES=		gmake
USE_EMACS=	yes
WRKSRC=		${WRKDIR}/egg-4.0.6+0.20041122cvs
GNU_CONFIGURE=	yes
CONFIGURE_ENV=	lispdir="${LOCALBASE}/${EMACS_VERSION_SITE_LISPDIR}"
PLIST_SUB=	ELISPDIR="${EMACS_VERSION_SITE_LISPDIR}"
PORTDOCS=	AUTHORS ChangeLog ChangeLog.1997-1998 \
		ChangeLog.2000-2001 PROBLEMS README.ja.txt TODO \
		README.Debian changelog.Debian
OPTIONS_DEFINE=	DOCS

.include <bsd.port.options.mk>

post-build:
	cd ${WRKSRC}/helper && \
	    ${SETENV} ${MAKE_ENV} ${MAKE} ${MAKE_FLAGS} ${MAKEFILE} \
	    ${_MAKE_JOBS} ${MAKE_ARGS} egg-helper
	${INSTALL_DATA} ${WRKSRC}/debian/changelog ${WRKSRC}/changelog.Debian
	${INSTALL_DATA} ${WRKSRC}/debian/README.Debian ${WRKSRC}

post-install:
	${INSTALL_PROGRAM} ${WRKSRC}/helper/egg-helper \
	    ${STAGEDIR}${PREFIX}/bin/egg-helper
.if ${PORT_OPTIONS:MDOCS}
	${MKDIR} ${STAGEDIR}${DOCSDIR}
	cd ${WRKSRC} && ${INSTALL_DATA} ${PORTDOCS} ${STAGEDIR}${DOCSDIR}
.endif

.include <bsd.port.mk>
