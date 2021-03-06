# Created by: Matthias Sund <m.sund@arcor.de>
# $FreeBSD$

PORTNAME=	upp
PORTVERSION=	5485
PORTREVISION=	2
CATEGORIES=	devel x11-toolkits
MASTER_SITES=	SF
DISTNAME=	${PORTNAME}-x11-src-${PORTVERSION}

MAINTAINER=	m.sund@arcor.de
COMMENT=	Ultimate++, a BSD-licensed, cross-platform, C/C++ RAD suite

LICENSE=	BSD2CLAUSE

LIB_DEPENDS=	libfreetype.so:${PORTSDIR}/print/freetype2 \
		libexpat.so:${PORTSDIR}/textproc/expat2 \
		libnotify.so:${PORTSDIR}/devel/libnotify

USES=		gmake
USE_XORG=	xft
USE_GNOME=	gtk20

WRKSRC=		${WRKDIR}/${DISTNAME}
BUILD_WRKSRC=	${WRKSRC}/uppsrc

MACRO_FLAGS=	-DflagGUI -DflagGCC -DflagSHARED -DflagPOSIX -DflagBSD -DflagFREEBSD

MAKE_ARGS=	UPPOUT="../_out/" OutFile="../theide" \
		Macro="${MACRO_FLAGS}" \
		LIBPATH="-L${LOCALBASE}/lib -L/usr/lib" \
		CINC="-I. -I${LOCALBASE}/include -I${LOCALBASE}/include/freetype2 \
		-I${LOCALBASE}/include/gtk-2.0 -I${LOCALBASE}/include/atk-1.0 \
		-I${LOCALBASE}/include/cairo -I${LOCALBASE}/include/gdk-pixbuf-2.0 \
		-I${LOCALBASE}/include/pango-1.0 -I${LOCALBASE}/include/glib-2.0 \
		-I${LOCALBASE}/lib/glib-2.0/include \
		-I${LOCALBASE}/include/libpng -I/usr/include"

PORTDATA=	bazaar examples reference tutorial uppsrc GCC.bm

DESKTOP_ENTRIES="TheIDE" "IDE for cross-platform C++ development" \
		"${DATADIR}/uppsrc/ide/theide-48.png" "theide" \
		"Development;IDE;GTK;" false

OPTIONS_DEFINE=	SDL OPENGL MYSQL PGSQL USEMALLOC
USEMALLOC_DESC=	Compile without U++ heap allocator

PLIST_FILES=	bin/theide

SDL_USE=	sql
OPENGL_USE=	gl
MYSQL_USE=	mysql=yes
PGSQL_USES=	pgsql

.include <bsd.port.options.mk>

.if ${PORT_OPTIONS:MUSEMALLOC}
MACRO_FLAGS+=	-DflagUSEMALLOC
.endif

.if ${ARCH} == "ia64" || ${ARCH} == "powerpc" || ${ARCH} == "sparc64"
BROKEN=		Does not compile on ia64, powerpc, or sparc64
.endif

pre-build: .SILENT
	${MV} ${BUILD_WRKSRC}/Makefile.in ${BUILD_WRKSRC}/Makefile
	${REINPLACE_CMD} -e '/^CC =/d;/^CFLAGS =/d;/^CXXFLAGS =/d;/^LDFLAGS =/d' \
	-e 's|$$(CC)|$$(CXX)|' \
	-e 's|-Linux-|-BSD-FreeBSD-|' \
	-e 's|-ldl|-lXau -lXdmcp -lfreetype -lexpat -lxcb -lpng|' \
	${BUILD_WRKSRC}/Makefile

post-build: .SILENT
	${ECHO_CMD} "BUILDER = \"GCC\"" > ${WRKSRC}/GCC.bm
	${ECHO_CMD} "DEBUG_INFO = \"0\";" >> ${WRKSRC}/GCC.bm
	${ECHO_CMD} "DEBUG_BLITZ = \"1\";" >> ${WRKSRC}/GCC.bm
	${ECHO_CMD} "DEBUG_LINKMODE = \"1\";" >> ${WRKSRC}/GCC.bm
	${ECHO_CMD} "DEBUG_OPTIONS = \"-O0\";" >> ${WRKSRC}/GCC.bm
	${ECHO_CMD} "DEBUG_FLAGS = \"\";" >> ${WRKSRC}/GCC.bm
	${ECHO_CMD} "DEBUG_LINK = \"\";" >> ${WRKSRC}/GCC.bm
	${ECHO_CMD} "RELEASE_BLITZ = \"0\";" >> ${WRKSRC}/GCC.bm
	${ECHO_CMD} "RELEASE_LINKMODE = \"1\";" >> ${WRKSRC}/GCC.bm
	${ECHO_CMD} "RELEASE_OPTIONS = \"-O2 -ffunction-sections\";" >> ${WRKSRC}/GCC.bm
	${ECHO_CMD} "RELEASE_SIZE_OPTIONS = \"-Os -finline-limit=20 -ffunction-sections\";" >> ${WRKSRC}/GCC.bm
	${ECHO_CMD} "DEBUGGER = \"gdb\";" >> ${WRKSRC}/GCC.bm
	${ECHO_CMD} "PATH = \"\";" >> ${WRKSRC}/GCC.bm
	${ECHO_CMD} "INCLUDE = \"${LOCALBASE}/include;${LOCALBASE}/include/freetype2;${LOCALBASE}/include/gtk-2.0;${LOCALBASE}/include/atk-1.0;${LOCALBASE}/include/cairo;${LOCALBASE}/include/gdk-pixbuf-2.0;${LOCALBASE}/include/pango-1.0;${LOCALBASE}/include/glib-2.0;${LOCALBASE}/include/libpng;/usr/include\";" >> ${WRKSRC}/GCC.bm
	${ECHO_CMD} "LIB = \"${LOCALBASE}/lib;/usr/lib\";" >> ${WRKSRC}/GCC.bm
	${ECHO_CMD} "REMOTE_HOST = \"\";" >> ${WRKSRC}/GCC.bm
	${ECHO_CMD} "REMOTE_OS = \"\";" >> ${WRKSRC}/GCC.bm
	${ECHO_CMD} "REMOTE_TRANSFER = \"\";" >> ${WRKSRC}/GCC.bm
	${ECHO_CMD} "REMOTE_MAP = \"\";" >> ${WRKSRC}/GCC.bm
	${ECHO_CMD} "LINKMODE_LOCK = \"0\";" >> ${WRKSRC}/GCC.bm

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/theide ${STAGEDIR}${PREFIX}/bin
	${MKDIR} ${STAGEDIR}${DATADIR}
	cd ${WRKSRC} && ${COPYTREE_SHARE} "${PORTDATA}" ${STAGEDIR}${DATADIR}

.include <bsd.port.mk>
