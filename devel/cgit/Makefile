# $FreeBSD$

PORTNAME=	cgit
PORTVERSION=	0.11.0
CATEGORIES=	devel www
MASTER_SITES=	http://git.zx2c4.com/cgit/snapshot/:cgit \
		https://www.kernel.org/pub/software/scm/git/:git
DISTFILES=	cgit-${PORTVERSION}${EXTRACT_SUFX}:cgit \
		git-${GIT_VERSION}.tar.gz:git

MAINTAINER=	kevinz5000@gmail.com
COMMENT=	Hyperfast web frontend for Git repositories

LICENSE=	GPLv2
LICENSE_FILE=	${WRKSRC}/COPYING

PROJECTHOST=	git-core
GIT_VERSION=	2.3.0
USES=		gmake iconv shebangfix tar:xz
SHEBANG_FILES=	filters/html-converters/resources/markdown.pl

CFLAGS+=	-I${LOCALBASE}/include
LDFLAGS+=	-L${LOCALBASE}/lib ${ICONV_LIB}
MAKE_ARGS+=	CGIT_SCRIPT_PATH=${WWWDIR} CGIT_CONFIG=${PREFIX}/etc/cgitrc \
		prefix=${PREFIX} NO_GETTEXT=1 NO_LUA=1

SUB_FILES=	pkg-message
SUB_LIST+=	PORTNAME=${PORTNAME}
PLIST_SUB+=	PORTNAME=${PORTNAME} WWWOWN=${WWWOWN} WWWGRP=${WWWGRP}

PORTDOCS=	${PORTNAME}rc.5.txt

OPTIONS_DEFINE=	DOCS

post-extract:
	@${RMDIR} ${WRKSRC}/git
	@${MV} ${WRKDIR}/git-${GIT_VERSION} ${WRKSRC}/git

post-patch:
	@${REINPLACE_CMD} -e 's/-liconv/${ICONV_LIB}/' ${WRKSRC}/git/Makefile

post-install:
	@${MKDIR} ${STAGEDIR}${DOCSDIR}
	${INSTALL_DATA} ${PORTDOCS:S|^|${WRKSRC}/|} ${STAGEDIR}${DOCSDIR}
	@${STRIP_CMD} ${STAGEDIR}${WWWDIR}/cgit.cgi

.include <bsd.port.mk>
